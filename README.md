
r/algotrading encyclopedia
I kept finding good strategy ideas buried in old r/algotrading threads and then losing them again, so I built this. It pulls a year of posts and comments, picks out the strategies, tools, brokers, data sources and performance claims people mention, and turns it all into a searchable knowledge base.

The idea is to feed the best of it into my backtesting framework (trading-v2) instead of testing random ideas.

Built with Python and SQLite. It runs fully offline by default, with an optional local LLM step (Ollama) for writing strategy summaries.

Step 1: collect
pip install -r requirements.txt
cd collector
python collect.py --after 2025-10-22 --before 2026-10-22 --out ../data/raw
python build_threads.py --raw ../data/raw --out ../data/threads
Data comes from the Arctic Shift archive (no API key needed). Comments are collected for 30 days past --before (--comment-grace-days) so late posts still get their replies. collect.py is resumable: re-run it after an interruption and it picks up from data/raw/state.json.

Step 2: extract (free, no API key)
cd extractor
python extract.py --threads ../data/threads --out ../data/extracted
The default rules backend uses the dictionary in extractor/lexicon.py (edit it to add terms) to find tools, data sources, brokers, strategy families, concepts, asset classes, timeframes and performance claims (Sharpe, CAGR, drawdown, win rate, profit factor) in every post and comment. It also scores each thread's strategy likelihood and how commenters reacted. A full year takes about a minute.

Optional: for written strategy summaries with entry/exit rules, install Ollama, run ollama pull qwen2.5:14b, then:

python extract.py --backend ollama --model qwen2.5:14b
That sends only threads that look like strategies (--llm-threshold, default 0.45) to the local model, keeps the rule results, and resumes where it left off if stopped. Smaller models such as qwen2.5:7b or llama3.1:8b are faster on modest hardware.

Step 3: build the encyclopedia
cd encyclopedia
python build.py                        # -> ../data/encyclopedia.db and ../output/*.md
python search.py "opening range breakout"
python search.py --top data_sources
python search.py --metric sharpe --min 1.5
output/README.md is the index: a strategy ranking, plus a page per tool, data source, broker, strategy family, concept, asset class and timeframe, each with its top threads, the entities it's discussed alongside, and the highest-voted quotes. Duplicate reposts are dropped.

Next steps
Export top strategies as specs for the backtester
