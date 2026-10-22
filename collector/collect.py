"""Collect r/algotrading posts and comments from the Arctic Shift archive.

Usage:
    python collect.py --after 2025-10-22 --before 2026-10-22 --out data/raw

Writes:
    <out>/posts.jsonl      one post per line
    <out>/comments.jsonl   one comment per line
    <out>/state.json       resume cursor per stream (safe to re-run)

Then run build_threads.py to group comments under their posts.
"""
import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone

import requests

API = "https://arctic-shift.photon-reddit.com/api"
PAGE = 100
POST_FIELDS = [
    "id", "title", "selftext", "author", "created_utc", "score",
    "num_comments", "link_flair_text", "url",
]
COMMENT_FIELDS = [
    "id", "link_id", "parent_id", "author", "body", "created_utc", "score",
]


def to_epoch(date_str):
    return int(datetime.strptime(date_str, "%Y-%m-%d").replace(tzinfo=timezone.utc).timestamp())


def get(session, path, params, retries=8):
    for attempt in range(retries):
        try:
            r = session.get(f"{API}/{path}", params=params, timeout=60)
            if r.status_code == 429 or r.status_code >= 500:
                raise requests.HTTPError(f"HTTP {r.status_code}")
            body = r.json()
            if "timeout" in str(body.get("error", "")).lower():
                # Archive is overloaded: back off and retry.
                raise requests.HTTPError(f"HTTP {r.status_code}: {body['error']}")
            if r.status_code >= 400 or body.get("error"):
                # Bad request (e.g. invalid field): retrying won't help.
                raise SystemExit(f"{path}: HTTP {r.status_code}: {body.get('error')}")
            return body.get("data") or []
        except (requests.RequestException, ValueError) as e:
            wait = min(2 ** attempt * 5, 300)
            print(f"  {path}: {e}; retrying in {wait}s", file=sys.stderr)
            time.sleep(wait)
    raise RuntimeError(f"giving up on {path} {params}")


def load_state(path):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return {}


def save_state(path, state):
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(state, f)
    os.replace(tmp, path)


def collect(session, kind, subreddit, after, before, out_path, state, state_path):
    """Page forward in time through `kind` ("posts" or "comments")."""
    fields = POST_FIELDS if kind == "posts" else COMMENT_FIELDS
    cursor = state.get(kind, after)
    seen_at_cursor = set(state.get(f"{kind}_seen", []))
    total = 0
    with open(out_path, "a") as out:
        while cursor < before:
            batch = get(session, f"{kind}/search", {
                "subreddit": subreddit,
                "after": cursor,
                "before": before,
                "limit": PAGE,
                "sort": "asc",
                "fields": ",".join(fields),
            })
            # Items sharing the cursor timestamp may be returned again; skip them.
            batch = [b for b in batch if b["id"] not in seen_at_cursor]
            if not batch:
                break
            for item in batch:
                out.write(json.dumps(item) + "\n")
            total += len(batch)
            last = int(batch[-1]["created_utc"])
            seen_at_cursor = {b["id"] for b in batch if int(b["created_utc"]) == last}
            if last == cursor:
                # Whole page at one timestamp: step past it to avoid looping.
                last += 1
                seen_at_cursor = set()
            cursor = last
            state[kind] = cursor
            state[f"{kind}_seen"] = sorted(seen_at_cursor)
            save_state(state_path, state)
            day = datetime.fromtimestamp(cursor, timezone.utc).strftime("%Y-%m-%d")
            print(f"{kind}: {total} collected, up to {day}")
            time.sleep(1)
    state[kind] = before
    save_state(state_path, state)
    return total


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--subreddit", default="algotrading")
    p.add_argument("--after", required=True, help="YYYY-MM-DD (UTC)")
    p.add_argument("--before", required=True, help="YYYY-MM-DD (UTC)")
    p.add_argument("--out", default="data/raw")
    p.add_argument("--skip-comments", action="store_true")
    p.add_argument("--comment-grace-days", type=int, default=30,
                   help="keep collecting comments this long after --before, so late posts get their replies")
    args = p.parse_args()

    os.makedirs(args.out, exist_ok=True)
    state_path = os.path.join(args.out, "state.json")
    state = load_state(state_path)
    after, before = to_epoch(args.after), to_epoch(args.before)

    session = requests.Session()
    session.headers["User-Agent"] = "algotrading-encyclopedia/0.1 (research)"

    n = collect(session, "posts", args.subreddit, after, before,
                os.path.join(args.out, "posts.jsonl"), state, state_path)
    print(f"posts done: {n} new")
    if not args.skip_comments:
        comments_before = min(before + args.comment_grace_days * 86400, int(time.time()))
        n = collect(session, "comments", args.subreddit, after, comments_before,
                    os.path.join(args.out, "comments.jsonl"), state, state_path)
        print(f"comments done: {n} new")


if __name__ == "__main__":
    main()
