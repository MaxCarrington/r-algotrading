"""Build the searchable encyclopedia from extracted records.

Usage:
    python build.py --extracted ../data/extracted --db ../data/encyclopedia.db --pages ../output

Produces:
    encyclopedia.db   SQLite with full-text search over threads, snippets,
                      strategies and lessons (query it with search.py)
    output/           Markdown pages: README index, strategy ranking, and one
                      page per tool, data source, broker, strategy family and concept
"""
import argparse
import glob
import json
import math
import os
import re
import sqlite3
from collections import defaultdict
from datetime import datetime, timezone

CATEGORY_TITLES = {
    "strategy_families": "Strategy families",
    "tools": "Tools and libraries",
    "data_sources": "Data sources",
    "brokers": "Brokers and venues",
    "concepts": "Concepts and pitfalls",
    "asset_classes": "Asset classes",
    "timeframes": "Timeframes",
}

SCHEMA = """
DROP TABLE IF EXISTS threads; DROP TABLE IF EXISTS mentions; DROP TABLE IF EXISTS metrics;
DROP TABLE IF EXISTS strategies; DROP TABLE IF EXISTS lessons; DROP TABLE IF EXISTS entities;
DROP TABLE IF EXISTS search;
CREATE TABLE threads (id TEXT PRIMARY KEY, title TEXT, url TEXT, created TEXT, score INT,
    num_comments INT, flair TEXT, likelihood REAL, rank_score REAL, families TEXT,
    skeptical INT, praising INT);
CREATE TABLE mentions (thread_id TEXT, category TEXT, entity TEXT, count INT, score_sum INT,
    in_post INT, snippets TEXT);
CREATE TABLE metrics (thread_id TEXT, metric TEXT, value REAL, source TEXT, score INT, context TEXT);
CREATE TABLE strategies (thread_id TEXT, name TEXT, summary TEXT, asset_class TEXT, timeframe TEXT,
    entry_rules TEXT, exit_rules TEXT, risk_management TEXT, claimed_results TEXT,
    tested_how TEXT, community_verdict TEXT, testability INT, signals TEXT);
CREATE TABLE lessons (thread_id TEXT, lesson TEXT);
CREATE TABLE entities (category TEXT, entity TEXT, threads INT, mentions INT, score_sum INT,
    weight REAL, PRIMARY KEY (category, entity));
CREATE VIRTUAL TABLE search USING fts5(kind, thread_id UNINDEXED, title, body);
"""


def strategy_rank(rec):
    """Score how worth-reading a thread is as a strategy source (higher is better)."""
    s = rec["strategy_signals"]
    rc = rec["reception"]
    engagement = math.log1p(max(rec["score"], 0)) + 0.5 * math.log1p(rc["comments"])
    has_post_metrics = any(m["source"] == "post" for m in rec["metrics"])
    # Skeptical replies lower the score unless praise offsets them.
    reception = 1 + 0.1 * rc["praising_comments"] - 0.05 * max(rc["skeptical_comments"] - rc["praising_comments"], 0)
    reception = min(max(reception, 0.5), 1.5)
    llm_bonus = 0
    if rec.get("llm", {}).get("strategies"):
        llm_bonus = max(st.get("testability", 0) for st in rec["llm"]["strategies"]) / 5
    return round(s["likelihood"] * engagement * reception * (1 + 0.3 * has_post_metrics + 0.5 * llm_bonus), 3)


def day(ts):
    return datetime.fromtimestamp(int(ts or 0), timezone.utc).strftime("%Y-%m-%d")


def slug(name):
    return re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def md_escape(s):
    return (s or "").replace("|", "\\|").replace("\n", " ")


def load(extracted):
    path = os.path.join(extracted, "all.jsonl")
    with open(path) as f:
        recs = [json.loads(line) for line in f]
    # People often repost the same thread (removed, then reposted). Keep the best-scoring copy.
    best = {}
    for r in recs:
        key = (r.get("author"), re.sub(r"[^a-z0-9]+", " ", (r["title"] or "").lower()).strip()[:60])
        if key[0] in (None, "[deleted]"):
            key = (r["id"], key[1])
        if key not in best or (r["score"], r["num_comments"]) > (best[key]["score"], best[key]["num_comments"]):
            best[key] = r
    print(f"{len(recs) - len(best)} duplicate reposts dropped")
    return list(best.values())


def build_db(recs, db_path):
    if os.path.exists(db_path):
        os.remove(db_path)
    db = sqlite3.connect(db_path)
    db.executescript(SCHEMA)
    agg = defaultdict(lambda: {"threads": 0, "mentions": 0, "score_sum": 0, "weight": 0.0})

    for r in recs:
        rank = strategy_rank(r)
        rc = r["reception"]
        db.execute("INSERT INTO threads VALUES (?,?,?,?,?,?,?,?,?,?,?,?)", (
            r["id"], r["title"], r["url"], day(r["created_utc"]), r["score"], r["num_comments"],
            r.get("flair"), r["strategy_signals"]["likelihood"], rank,
            ", ".join(r["strategy_signals"]["families_in_post"]), rc["skeptical_comments"], rc["praising_comments"]))
        db.execute("INSERT INTO search VALUES ('thread', ?, ?, ?)", (r["id"], r["title"], r["title"]))

        for cat, ents in r["mentions"].items():
            for name, h in ents.items():
                db.execute("INSERT INTO mentions VALUES (?,?,?,?,?,?,?)", (
                    r["id"], cat, name, h["count"], h["score_sum"], int(h["in_post"]), json.dumps(h["snippets"])))
                a = agg[(cat, name)]
                a["threads"] += 1
                a["mentions"] += h["count"]
                a["score_sum"] += h["score_sum"]
                a["weight"] += h["count"] * (1 + math.log1p(max(r["score"], 0)))
                for sn in h["snippets"]:
                    db.execute("INSERT INTO search VALUES ('snippet', ?, ?, ?)", (r["id"], name, sn["text"]))

        for m in r["metrics"]:
            db.execute("INSERT INTO metrics VALUES (?,?,?,?,?,?)", (
                r["id"], m["metric"], m["value"], m["source"], m["score"], m["context"]))

        llm = r.get("llm") or {}
        for st in llm.get("strategies", []):
            db.execute("INSERT INTO strategies VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (
                r["id"], st.get("name"), st.get("summary"), st.get("asset_class"), st.get("timeframe"),
                st.get("entry_rules"), st.get("exit_rules"), st.get("risk_management"),
                st.get("claimed_results"), st.get("tested_how"), st.get("community_verdict"),
                st.get("testability"), json.dumps(st.get("indicators_or_signals", []))))
            db.execute("INSERT INTO search VALUES ('strategy', ?, ?, ?)", (
                r["id"], st.get("name"), " ".join(str(st.get(k, "")) for k in
                                                  ("summary", "entry_rules", "exit_rules", "claimed_results"))))
        for lesson in llm.get("lessons", []):
            db.execute("INSERT INTO lessons VALUES (?,?)", (r["id"], lesson))
            db.execute("INSERT INTO search VALUES ('lesson', ?, ?, ?)", (r["id"], r["title"], lesson))

    for (cat, name), a in agg.items():
        db.execute("INSERT INTO entities VALUES (?,?,?,?,?,?)",
                   (cat, name, a["threads"], a["mentions"], a["score_sum"], round(a["weight"], 1)))
    db.commit()
    return db


def write_pages(db, out):
    os.makedirs(out, exist_ok=True)
    q = db.execute
    n_threads = q("SELECT COUNT(*) FROM threads").fetchone()[0]
    span = q("SELECT MIN(created), MAX(created) FROM threads").fetchone()

    # Strategy ranking
    lines = ["# Strategy ranking", "",
             "Threads most likely to contain a usable strategy, ranked by strategy likelihood, "
             "engagement, community reception and whether results were reported.", "",
             "| # | Rank | Thread | Families | Score | Comments | Skeptical / praising | Post metrics |",
             "|---|---|---|---|---|---|---|---|"]
    rows = q("""SELECT t.*, (SELECT GROUP_CONCAT(metric || '=' || value, '; ') FROM metrics m
                WHERE m.thread_id = t.id AND m.source = 'post') FROM threads t
                WHERE likelihood >= 0.45 ORDER BY rank_score DESC LIMIT 300""").fetchall()
    for i, r in enumerate(rows, 1):
        lines.append(f"| {i} | {r[8]} | [{md_escape(r[1])}]({r[2]}) ({r[3]}) | {md_escape(r[9])} | {r[4]} | "
                     f"{r[5]} | {r[10]} / {r[11]} | {md_escape(r[12])[:120]} |")
    with open(os.path.join(out, "strategy-ranking.md"), "w") as f:
        f.write("\n".join(lines) + "\n")

    # LLM strategies, if any
    strategies = q("""SELECT s.*, t.title, t.url, t.score FROM strategies s JOIN threads t ON t.id = s.thread_id
                      ORDER BY s.testability DESC, t.rank_score DESC""").fetchall()
    if strategies:
        lines = ["# Strategy cards", "", "Written by the local LLM from each thread. Verify against the source.", ""]
        for s in strategies:
            lines += [f"## {s[1]}", f"Source: [{md_escape(s[13])}]({s[14]}) (score {s[15]}) · testability {s[11]}/5", "",
                      s[2] or "", ""]
            for label, idx in (("Asset class", 3), ("Timeframe", 4), ("Entry", 5), ("Exit", 6), ("Risk", 7),
                               ("Claimed results", 8), ("Tested how", 9), ("Community verdict", 10)):
                if s[idx]:
                    lines.append(f"- **{label}:** {s[idx]}")
            lines.append("")
        with open(os.path.join(out, "strategy-cards.md"), "w") as f:
            f.write("\n".join(lines) + "\n")

    # Entity pages
    index = [f"# r/algotrading encyclopedia", "",
             f"Built from {n_threads} threads, {span[0]} to {span[1]}.", "",
             "- [Strategy ranking](strategy-ranking.md)"]
    if strategies:
        index.append("- [Strategy cards](strategy-cards.md)")
    lessons = q("SELECT COUNT(*) FROM lessons").fetchone()[0]
    if lessons:
        index.append("- [Lessons](lessons.md)")
        rows = q("""SELECT l.lesson, t.title, t.url, t.score FROM lessons l JOIN threads t ON t.id = l.thread_id
                    ORDER BY t.score DESC""").fetchall()
        with open(os.path.join(out, "lessons.md"), "w") as f:
            f.write("# Lessons\n\n" + "\n".join(f"- {l} ([{md_escape(t)}]({u}), score {s})" for l, t, u, s in rows) + "\n")

    for cat, title in CATEGORY_TITLES.items():
        os.makedirs(os.path.join(out, cat), exist_ok=True)
        ents = q("SELECT entity, threads, mentions, score_sum, weight FROM entities WHERE category = ? "
                 "ORDER BY weight DESC", (cat,)).fetchall()
        index += ["", f"## {title}", "", "| Name | Threads | Mentions | Upvotes on mentions |", "|---|---|---|---|"]
        for name, threads, mentions, score_sum, _ in ents:
            index.append(f"| [{name}]({cat}/{slug(name)}.md) | {threads} | {mentions} | {score_sum} |")
            write_entity_page(db, out, cat, name, threads, mentions)

    with open(os.path.join(out, "README.md"), "w") as f:
        f.write("\n".join(index) + "\n")


def write_entity_page(db, out, cat, name, threads, mentions):
    q = db.execute
    lines = [f"# {name}", "", f"Mentioned {mentions} times across {threads} threads. [Back to index](../README.md)", ""]

    co = q("""SELECT m2.category, m2.entity, COUNT(*) c FROM mentions m1 JOIN mentions m2
              ON m1.thread_id = m2.thread_id AND NOT (m2.category = m1.category AND m2.entity = m1.entity)
              WHERE m1.category = ? AND m1.entity = ? AND m2.category IN
              ('tools','data_sources','brokers','strategy_families','asset_classes')
              GROUP BY 1, 2 ORDER BY c DESC LIMIT 12""", (cat, name)).fetchall()
    if co:
        lines += ["**Often discussed with:** " + ", ".join(
            f"[{e}](../{c}/{slug(e)}.md) ({n})" for c, e, n in co), ""]

    lines += ["## Top threads", ""]
    rows = q("""SELECT t.title, t.url, t.created, t.score, m.count, m.in_post FROM mentions m
                JOIN threads t ON t.id = m.thread_id WHERE m.category = ? AND m.entity = ?
                ORDER BY MAX(t.score, 0) * (1 + m.in_post) + m.count DESC LIMIT 25""", (cat, name)).fetchall()
    for title, url, created, score, count, in_post in rows:
        where = "in post" if in_post else f"{count} comments"
        lines.append(f"- [{md_escape(title)}]({url}) · {created} · score {score} · {where}")

    lines += ["", "## What people said", ""]
    rows = q("""SELECT m.snippets, t.url FROM mentions m JOIN threads t ON t.id = m.thread_id
                WHERE m.category = ? AND m.entity = ?""", (cat, name)).fetchall()
    snips = [(s, url) for js, url in rows for s in json.loads(js)]
    snips.sort(key=lambda x: -x[0]["score"])
    for s, url in snips[:20]:
        link = url if s["source"] == "post" else f"{url}_/{s['source']}/"
        lines.append(f"> {md_escape(s['text'])}  \n> [score {s['score']}]({link})\n")

    with open(os.path.join(out, cat, f"{slug(name)}.md"), "w") as f:
        f.write("\n".join(lines) + "\n")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--extracted", default="../data/extracted")
    p.add_argument("--db", default="../data/encyclopedia.db")
    p.add_argument("--pages", default="../output")
    args = p.parse_args()
    recs = load(args.extracted)
    db = build_db(recs, args.db)
    write_pages(db, args.pages)
    print(f"{len(recs)} threads indexed into {args.db}; pages written to {args.pages}")


if __name__ == "__main__":
    main()
