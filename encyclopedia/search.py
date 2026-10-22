"""Search the encyclopedia from the command line.

Usage:
    python search.py "opening range breakout"
    python search.py "databento OR polygon" --kind snippet --limit 30
    python search.py --top tools          # most discussed entities in a category
    python search.py --metric sharpe --min 1.5

Query syntax is SQLite FTS5: phrases in quotes, AND / OR / NOT, prefix*.
"""
import argparse
import sqlite3


def main():
    p = argparse.ArgumentParser()
    p.add_argument("query", nargs="?")
    p.add_argument("--db", default="../data/encyclopedia.db")
    p.add_argument("--kind", choices=["thread", "snippet", "strategy", "lesson"])
    p.add_argument("--limit", type=int, default=20)
    p.add_argument("--top", help="category: tools, data_sources, brokers, strategy_families, concepts, ...")
    p.add_argument("--metric", help="sharpe, sortino, cagr_pct, max_drawdown_pct, win_rate_pct, profit_factor")
    p.add_argument("--min", type=float, default=float("-inf"))
    args = p.parse_args()
    db = sqlite3.connect(args.db)

    if args.top:
        for e, t, m, s in db.execute("SELECT entity, threads, mentions, score_sum FROM entities WHERE category = ? "
                                     "ORDER BY weight DESC LIMIT ?", (args.top, args.limit)):
            print(f"{e:40} {t:5} threads {m:6} mentions {s:7} upvotes")
        return

    if args.metric:
        for v, sc, ctx, title, url in db.execute(
                """SELECT m.value, m.score, m.context, t.title, t.url FROM metrics m JOIN threads t ON t.id = m.thread_id
                   WHERE m.metric = ? AND m.value >= ? ORDER BY m.score DESC LIMIT ?""",
                (args.metric, args.min, args.limit)):
            print(f"{args.metric}={v}  (score {sc})  {title}\n  {ctx}\n  {url}\n")
        return

    if not args.query:
        p.error("give a query, --top or --metric")
    sql = """SELECT s.kind, s.title, snippet(search, 3, '[', ']', '...', 24), t.url, t.score
             FROM search s JOIN threads t ON t.id = s.thread_id WHERE search MATCH ?"""
    params = [args.query]
    if args.kind:
        sql += " AND s.kind = ?"
        params.append(args.kind)
    sql += " ORDER BY bm25(search) - log(1 + max(t.score, 0)) LIMIT ?"
    params.append(args.limit)
    for kind, title, snip, url, score in db.execute(sql, params):
        print(f"[{kind}] {title}  (score {score})\n  {snip}\n  {url}\n")


if __name__ == "__main__":
    main()
