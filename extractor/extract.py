"""Extract structured knowledge from collected threads. No paid API needed.

Two backends:
  rules   (default) Dictionary + regex extraction. Fast, free, runs anywhere.
          Finds tools, data sources, brokers, strategy families, concepts,
          asset classes, timeframes, and performance claims (Sharpe, CAGR...).
  ollama  Rules PLUS a local LLM (via Ollama, free) that writes strategy
          summaries with entry/exit rules, lessons and community verdicts.
          Slower; only runs on threads that look like they contain a strategy
          unless --llm-all is passed.

Usage:
    python extract.py --threads ../data/threads --out ../data/extracted
    python extract.py --backend ollama --model qwen2.5:14b --min-score 5

Output: one <post_id>.json per thread in --out, plus all.jsonl combining them.
Re-running skips threads already extracted (use --force to redo).
"""
import argparse
import glob
import json
import os
import re
import sys
from collections import defaultdict

from lexicon import CATEGORIES

SNIPPET_CHARS = 220
MAX_SNIPPETS = 3


# --------------------------------------------------------------------------- rules

def compile_lexicon():
    compiled = {}
    for cat, entries in CATEGORIES.items():
        compiled[cat] = {}
        for name, aliases in entries.items():
            pats = []
            for a in aliases:
                flags = re.IGNORECASE
                if a.startswith("(?-i)"):
                    a, flags = a[5:], 0
                pats.append(re.compile(rf"(?<!\w)(?:{a})(?!\w)", flags))
            compiled[cat][name] = pats
    return compiled


METRIC_PATTERNS = {
    "sharpe": re.compile(r"sharpe(?:\s*ratio)?\s*(?:of|=|:|~|≈|is|was|around|of about|near)?\s*(-?\d+(?:\.\d+)?)", re.I),
    "sortino": re.compile(r"sortino\s*(?:of|=|:|~|is|was)?\s*(-?\d+(?:\.\d+)?)", re.I),
    "cagr_pct": re.compile(r"(?:cagr|annual(?:ized)? returns?|per year|/yr|/year|a year)\D{0,20}?(-?\d+(?:\.\d+)?)\s*%"
                           r"|(-?\d+(?:\.\d+)?)\s*%\s*(?:cagr|annual(?:ized)?|per year|/yr|/year|a year)", re.I),
    "max_drawdown_pct": re.compile(r"(?:max(?:imum)?\s*)?(?:drawdown|\bdd\b|mdd)\D{0,20}?(-?\d+(?:\.\d+)?)\s*%"
                                   r"|(-?\d+(?:\.\d+)?)\s*%\s*(?:max(?:imum)?\s*)?(?:drawdown|dd\b)", re.I),
    "win_rate_pct": re.compile(r"win\s*rate\D{0,15}?(\d+(?:\.\d+)?)\s*%|(\d+(?:\.\d+)?)\s*%\s*win\s*rate", re.I),
    "profit_factor": re.compile(r"profit\s*factor\s*(?:of|=|:|~|is|was)?\s*(\d+(?:\.\d+)?)", re.I),
}

RULE_HINTS = re.compile(
    r"\b(?:buy|go long|enter|entry|short|sell|exit)\b[^.\n]{0,60}\b(?:when|if|after|once|on|at)\b"
    r"|\b(?:stop[- ]loss|take[- ]profit|trailing stop|holding period|rebalanc\w*)\b"
    r"|\b(?:crosses (?:above|below)|closes? (?:above|below)|lookback)\b", re.I)
RESULT_HINTS = re.compile(r"\b(?:backtest\w*|out[- ]of[- ]sample|live (?:trading|results?)|forward test\w*|"
                          r"paper trad\w*|returns?|sharpe|drawdown|cagr|equity curve)\b", re.I)
SKEPTIC_HINTS = re.compile(r"\b(?:overfit\w*|curve[- ]fit\w*|look-?ahead|survivorship|too good to be true|"
                           r"won'?t work|doesn'?t work|scam|bias|data[- ]snoop\w*|in[- ]sample)\b", re.I)
PRAISE_HINTS = re.compile(r"\b(?:great (?:post|write-?up|work)|thanks for sharing|this is gold|"
                          r"underrated|solid|well done|really useful|very helpful|saved)\b", re.I)


def flatten(comments, depth=0):
    for c in comments:
        yield c, depth
        yield from flatten(c.get("replies", []), depth + 1)


def snippet(text, m):
    start = max(0, m.start() - SNIPPET_CHARS // 2)
    s = text[start:start + SNIPPET_CHARS].replace("\n", " ").strip()
    return ("..." if start else "") + s + "..."


def extract_rules(thread, lex):
    post_text = f"{thread.get('title', '')}\n\n{thread.get('selftext') or ''}"
    comments = list(flatten(thread.get("comments", [])))
    sources = [("post", post_text, thread.get("score", 0))] + \
              [(c["id"], c["body"], c.get("score", 0)) for c, _ in comments]

    mentions = {}
    for cat, entries in lex.items():
        found = {}
        for name, pats in entries.items():
            hit = {"count": 0, "in_post": False, "comment_ids": [], "score_sum": 0, "snippets": []}
            for src_id, text, score in sources:
                m = next((m for p in pats for m in [p.search(text)] if m), None)
                if not m:
                    continue
                hit["count"] += 1
                hit["score_sum"] += max(score, 0)
                if src_id == "post":
                    hit["in_post"] = True
                else:
                    hit["comment_ids"].append(src_id)
                if len(hit["snippets"]) < MAX_SNIPPETS:
                    hit["snippets"].append({"source": src_id, "score": score, "text": snippet(text, m)})
            if hit["count"]:
                found[name] = hit
        mentions[cat] = found

    metrics = []
    for src_id, text, score in sources:
        for kind, pat in METRIC_PATTERNS.items():
            for m in pat.finditer(text):
                val = next(g for g in m.groups() if g is not None)
                metrics.append({"metric": kind, "value": float(val), "source": src_id,
                                "score": score, "context": snippet(text, m)})

    comment_texts = [c["body"] for c, _ in comments]
    skeptic = sum(bool(SKEPTIC_HINTS.search(t)) for t in comment_texts)
    praise = sum(bool(PRAISE_HINTS.search(t)) for t in comment_texts)
    families = mentions["strategy_families"]
    in_post_families = [n for n, h in families.items() if h["in_post"]]
    has_rules = bool(RULE_HINTS.search(post_text))
    has_results = bool(RESULT_HINTS.search(post_text))
    flair = (thread.get("link_flair_text") or "").lower()
    likelihood = min(1.0, 0.3 * bool(in_post_families) + 0.25 * has_rules + 0.2 * has_results
                     + 0.15 * bool([m for m in metrics if m["source"] == "post"])
                     + 0.1 * (flair == "strategy"))

    return {
        "mentions": mentions,
        "metrics": metrics,
        "strategy_signals": {
            "families_in_post": in_post_families,
            "has_rules": has_rules,
            "has_results": has_results,
            "likelihood": round(likelihood, 2),
        },
        "reception": {
            "post_score": thread.get("score", 0),
            "comments": len(comments),
            "skeptical_comments": skeptic,
            "praising_comments": praise,
            "top_comment_score": max((c.get("score", 0) for c, _ in comments), default=0),
        },
    }


# --------------------------------------------------------------------------- ollama

LLM_SCHEMA = {
    "type": "object",
    "properties": {
        "strategies": {"type": "array", "items": {"type": "object", "properties": {
            "name": {"type": "string"},
            "summary": {"type": "string"},
            "asset_class": {"type": "string"},
            "timeframe": {"type": "string"},
            "indicators_or_signals": {"type": "array", "items": {"type": "string"}},
            "entry_rules": {"type": "string"},
            "exit_rules": {"type": "string"},
            "risk_management": {"type": "string"},
            "claimed_results": {"type": "string"},
            "tested_how": {"type": "string", "description": "backtest, paper, live, idea only"},
            "community_verdict": {"type": "string", "description": "how commenters reacted and why"},
            "testability": {"type": "integer", "description": "1-5, how fully specified the rules are"},
        }, "required": ["name", "summary", "entry_rules", "exit_rules", "testability"]}},
        "lessons": {"type": "array", "items": {"type": "string"}},
        "tools_opinions": {"type": "array", "items": {"type": "object", "properties": {
            "name": {"type": "string"}, "opinion": {"type": "string"}}}},
        "data_source_opinions": {"type": "array", "items": {"type": "object", "properties": {
            "name": {"type": "string"}, "opinion": {"type": "string"}}}},
    },
    "required": ["strategies", "lessons", "tools_opinions", "data_source_opinions"],
}

LLM_PROMPT = """You are building an encyclopedia of algorithmic trading knowledge from a Reddit r/algotrading thread.
Extract ONLY what is actually stated in the thread. Do not invent rules or numbers. Use "" for unknown fields.

- strategies: every concrete trading strategy described in the post or comments, with as much rule detail as given.
  If the post only asks a question and no strategy is described, return an empty list.
- lessons: practical, reusable insights (e.g. "re-check results at double transaction costs").
- tools_opinions / data_source_opinions: libraries, platforms, data vendors and what people said about them.

THREAD:
{text}
"""


def thread_text(thread, budget):
    parts = [f"TITLE: {thread.get('title', '')}",
             f"POST (score {thread.get('score', 0)}):\n{thread.get('selftext') or ''}", "COMMENTS:"]
    used = sum(len(p) for p in parts)
    for c, depth in flatten(thread.get("comments", [])):
        line = f"{'  ' * depth}- [score {c.get('score', 0)}] {c['body']}"
        if used + len(line) > budget:
            break
        parts.append(line)
        used += len(line)
    return "\n".join(parts)


def extract_ollama(thread, model, host, budget):
    import requests
    r = requests.post(f"{host}/api/chat", timeout=600, json={
        "model": model,
        "messages": [{"role": "user", "content": LLM_PROMPT.format(text=thread_text(thread, budget))}],
        "format": LLM_SCHEMA,
        "stream": False,
        "options": {"temperature": 0, "num_ctx": 16384},
    })
    r.raise_for_status()
    return json.loads(r.json()["message"]["content"])


# --------------------------------------------------------------------------- main

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--threads", default="../data/threads")
    p.add_argument("--out", default="../data/extracted")
    p.add_argument("--backend", choices=["rules", "ollama"], default="rules")
    p.add_argument("--model", default="qwen2.5:14b", help="any Ollama model with JSON output")
    p.add_argument("--ollama-host", default=os.environ.get("OLLAMA_HOST", "http://localhost:11434"))
    p.add_argument("--char-budget", type=int, default=24000, help="max thread chars sent to the LLM")
    p.add_argument("--min-score", type=int, default=0, help="skip posts below this score")
    p.add_argument("--llm-threshold", type=float, default=0.45,
                   help="only send threads with strategy likelihood >= this to the LLM")
    p.add_argument("--llm-all", action="store_true", help="send every thread to the LLM")
    p.add_argument("--force", action="store_true")
    args = p.parse_args()

    os.makedirs(args.out, exist_ok=True)
    lex = compile_lexicon()
    files = sorted(glob.glob(os.path.join(args.threads, "*.json")))
    done = skipped = llm_calls = 0

    for i, path in enumerate(files, 1):
        thread = json.load(open(path))
        out_path = os.path.join(args.out, f"{thread['id']}.json")
        if thread.get("score", 0) < args.min_score:
            skipped += 1
            continue
        existing = json.load(open(out_path)) if os.path.exists(out_path) else None
        needs_llm = args.backend == "ollama" and not (existing and "llm" in existing)
        if needs_llm and existing and not args.llm_all and \
                existing["strategy_signals"]["likelihood"] < args.llm_threshold:
            needs_llm = False
        if existing and not args.force and not needs_llm:
            continue

        rec = {
            "id": thread["id"],
            "title": thread.get("title"),
            "url": f"https://www.reddit.com/r/algotrading/comments/{thread['id']}/",
            "created_utc": thread.get("created_utc"),
            "score": thread.get("score", 0),
            "num_comments": thread.get("num_comments", 0),
            "flair": thread.get("link_flair_text"),
            "author": thread.get("author"),
            **extract_rules(thread, lex),
        }
        if existing and "llm" in existing and not args.force:
            rec["llm"] = existing["llm"]

        if needs_llm and (args.llm_all or rec["strategy_signals"]["likelihood"] >= args.llm_threshold):
            try:
                rec["llm"] = extract_ollama(thread, args.model, args.ollama_host, args.char_budget)
                rec["llm_model"] = args.model
                llm_calls += 1
            except Exception as e:  # keep going; rerun later picks it up
                print(f"  LLM failed on {thread['id']}: {e}", file=sys.stderr)

        with open(out_path, "w") as f:
            json.dump(rec, f)
        done += 1
        if i % 200 == 0 or llm_calls and llm_calls % 10 == 0:
            print(f"{i}/{len(files)} processed ({llm_calls} LLM calls)")

    with open(os.path.join(args.out, "all.jsonl"), "w") as f:
        for path in sorted(glob.glob(os.path.join(args.out, "*.json"))):
            f.write(open(path).read().strip() + "\n")

    print(f"done: {done} extracted, {skipped} below min score, {llm_calls} LLM calls")


if __name__ == "__main__":
    main()
