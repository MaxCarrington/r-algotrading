# r/algotrading encyclopedia

Turns a year of r/algotrading posts and comments into a searchable knowledge base of
strategy ideas, rankings, tools and data sources.

## Step 1: collect

```bash
pip install -r requirements.txt
cd collector
python collect.py --after 2025-10-22 --before 2026-10-22 --out ../data/raw
python build_threads.py --raw ../data/raw --out ../data/threads
```

Data comes from the [Arctic Shift](https://github.com/ArthurHeitmann/arctic_shift) archive
(no API key needed). Comments are collected for 30 days past `--before` (`--comment-grace-days`) so late posts still get their replies. `collect.py` is resumable: re-run it after an interruption and it picks
up from `data/raw/state.json`.

## Step 2: extract (free, no API key)

```bash
cd extractor
python extract.py --threads ../data/threads --out ../data/extracted
```

The default `rules` backend uses the dictionary in `extractor/lexicon.py` (edit it to add terms) to find
tools, data sources, brokers, strategy families, concepts, asset classes, timeframes and performance
claims (Sharpe, CAGR, drawdown, win rate, profit factor) in every post and comment. It also scores each
thread's strategy likelihood and how commenters reacted. A full year takes about a minute.

Optional: for written strategy summaries with entry/exit rules, install [Ollama](https://ollama.com),
run `ollama pull qwen2.5:14b`, then:

```bash
python extract.py --backend ollama --model qwen2.5:14b
```

That sends only threads that look like strategies (`--llm-threshold`, default 0.45) to the local
model, keeps the rule results, and resumes where it left off if stopped. Smaller models such as
`qwen2.5:7b` or `llama3.1:8b` are faster on modest hardware.

## Step 3: build the encyclopedia

```bash
cd encyclopedia
python build.py                        # -> ../data/encyclopedia.db and ../output/*.md
python search.py "opening range breakout"
python search.py --top data_sources
python search.py --metric sharpe --min 1.5
```

`output/README.md` is the index: a strategy ranking, plus a page per tool, data source, broker,
strategy family, concept, asset class and timeframe, each with its top threads, the entities it's
discussed alongside, and the highest-voted quotes. Duplicate reposts are dropped.

## Next steps

4. Export top strategies as specs for the backtester
