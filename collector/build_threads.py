"""Group raw comments under their posts into one JSON file per thread.

Usage:
    python build_threads.py --raw data/raw --out data/threads

Each output file <post_id>.json holds the post plus a nested comment tree,
sorted by score, ready for the extraction step. Deleted/removed comments
are dropped.
"""
import argparse
import json
import os
from collections import defaultdict

DEAD = {"[deleted]", "[removed]", ""}


def read_jsonl(path):
    items = {}
    if not os.path.exists(path):
        return items
    with open(path) as f:
        for line in f:
            item = json.loads(line)
            items[item["id"]] = item  # last write wins, dedupes re-runs
    return list(items.values())


def build_tree(comments):
    children = defaultdict(list)
    for c in comments:
        children[c["parent_id"]].append(c)

    def node(c):
        kids = sorted(children.get(f"t1_{c['id']}", []), key=lambda k: -k.get("score", 0))
        return {
            "id": c["id"], "author": c.get("author"), "score": c.get("score", 0),
            "body": c["body"], "replies": [node(k) for k in kids],
        }

    return children, node


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--raw", default="data/raw")
    p.add_argument("--out", default="data/threads")
    args = p.parse_args()

    posts = read_jsonl(os.path.join(args.raw, "posts.jsonl"))
    comments = [c for c in read_jsonl(os.path.join(args.raw, "comments.jsonl"))
                if c.get("body", "").strip() not in DEAD]

    by_post = defaultdict(list)
    for c in comments:
        by_post[c["link_id"].removeprefix("t3_")].append(c)

    os.makedirs(args.out, exist_ok=True)
    for post in posts:
        cs = by_post.get(post["id"], [])
        children, node = build_tree(cs)
        top = sorted(children.get(f"t3_{post['id']}", []), key=lambda k: -k.get("score", 0))
        thread = {**post, "comment_count_collected": len(cs), "comments": [node(c) for c in top]}
        with open(os.path.join(args.out, f"{post['id']}.json"), "w") as f:
            json.dump(thread, f)

    attached = sum(len(by_post.get(p["id"], [])) for p in posts)
    print(f"{len(posts)} threads written, {attached} comments attached "
          f"({len(comments) - attached} belonged to posts outside the date range)")


if __name__ == "__main__":
    main()
