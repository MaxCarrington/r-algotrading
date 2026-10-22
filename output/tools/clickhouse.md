# ClickHouse

Mentioned 45 times across 26 threads. [Back to index](../README.md)

**Often discussed with:** [Python](../tools/python.md) (18), [US equities](../asset_classes/us-equities.md) (17), [Parquet](../tools/parquet.md) (17), [Options](../asset_classes/options.md) (16), [Futures](../asset_classes/futures.md) (15), [Order flow / microstructure](../strategy_families/order-flow-microstructure.md) (15), [Crypto](../asset_classes/crypto.md) (14), [Interactive Brokers](../brokers/interactive-brokers.md) (14), [Alpaca](../brokers/alpaca.md) (12), [Alpaca (data)](../data_sources/alpaca-data.md) (12), [Databento](../data_sources/databento.md) (11), [pandas](../tools/pandas.md) (10)

## Top threads

- [Stop paying for Polymarket data. PMXT just open-sourced the orderbooks.](https://www.reddit.com/r/algotrading/comments/1rdhw2n/) · 2026-02-24 · score 556 · 1 comments
- [After about 4 years of exploration and 1.5 year of persistent effort, I think we finally have a "system"](https://www.reddit.com/r/algotrading/comments/1qklj4o/) · 2026-01-23 · score 246 · 1 comments
- [Got tired of TradingView’s limitations, so I built my own](https://www.reddit.com/r/algotrading/comments/1wgbj50/) · 2026-09-14 · score 205 · 1 comments
- [CLI tool for pulling historical Binance OHLCV data for backtesting](https://www.reddit.com/r/algotrading/comments/1qncdrx/) · 2026-01-26 · score 111 · 2 comments
- [The absolute nightmare of "premium" historical data](https://www.reddit.com/r/algotrading/comments/1tw23l4/) · 2026-06-03 · score 70 · 1 comments
- [What does everyone use for backtesting?](https://www.reddit.com/r/algotrading/comments/1pmktlg/) · 2025-12-14 · score 55 · 1 comments
- [Spent way too long building a financial database, now I don't know what to do with it](https://www.reddit.com/r/algotrading/comments/1w6r0g6/) · 2026-09-04 · score 46 · 2 comments
- [Personal algo trading platform I've been working on](https://www.reddit.com/r/algotrading/comments/1t1hpq4/) · 2026-05-02 · score 45 · 2 comments
- [Algotrading feels like Data Engineering](https://www.reddit.com/r/algotrading/comments/1qyohsj/) · 2026-02-07 · score 43 · 1 comments
- [How do retail algo traders actually run their systems?](https://www.reddit.com/r/algotrading/comments/1s439l3/) · 2026-03-26 · score 43 · 1 comments
- [Build your own trading bot / platform](https://www.reddit.com/r/algotrading/comments/1pydn9s/) · 2025-12-29 · score 34 · 5 comments
- [The algo trading data model I wish existed when I started — 4 layers, 12 tables, 3 dashboards](https://www.reddit.com/r/algotrading/comments/1td3ah3/) · 2026-05-14 · score 28 · 2 comments
- [How do you handle tick-level data storage without putting it in a relational DB?](https://www.reddit.com/r/algotrading/comments/1q6evvc/) · 2026-01-07 · score 21 · 1 comments
- [System Design](https://www.reddit.com/r/algotrading/comments/1tk16sq/) · 2026-05-21 · score 21 · 1 comments
- [What API feeds do you rely on?](https://www.reddit.com/r/algotrading/comments/1tlx366/) · 2026-05-24 · score 21 · 1 comments
- [Your Algo Tech Stack](https://www.reddit.com/r/algotrading/comments/1u9xae8/) · 2026-06-19 · score 14 · 1 comments
- [Level 2 Ticker Data](https://www.reddit.com/r/algotrading/comments/1vdsc8o/) · 2026-08-02 · score 13 · 2 comments
- [Rookie questions](https://www.reddit.com/r/algotrading/comments/1u0i56x/) · 2026-06-08 · score 9 · 1 comments
- [bottleneck at writing to disk on huge backtests](https://www.reddit.com/r/algotrading/comments/1p4sb7p/) · 2025-11-23 · score 6 · 3 comments
- [Anyone here automating in Sierra Chart? How do you handle backtesting?](https://www.reddit.com/r/algotrading/comments/1s7vvc6/) · 2026-03-30 · score 1 · 6 comments
- [Getting data for natural gas futures](https://www.reddit.com/r/algotrading/comments/1r320ev/) · 2026-02-12 · score 5 · 1 comments
- [Storage space constraints for market data](https://www.reddit.com/r/algotrading/comments/1uoulsl/) · 2026-07-06 · score 3 · 2 comments
- [How to Organize and Store Data?](https://www.reddit.com/r/algotrading/comments/1tzpk3p/) · 2026-06-07 · score 3 · 1 comments
- [I've created a monster](https://www.reddit.com/r/algotrading/comments/1vhwu16/) · 2026-08-07 · score 0 · 3 comments
- [meticulously recording my algo's outputs, today and everyday](https://www.reddit.com/r/algotrading/comments/1wskcda/) · 2026-09-28 · score 1 · 1 comments

## What people said

> ...FPM), with Slim for HTTP routing. * **Persistence:** Doctrine ORM + DBAL on Postgres for transactional state; ClickHouse for time-series (candles, ticks, trades, equity curves). * **Workflow engine:** Temporal orchestrat...  
> [score 12](https://www.reddit.com/r/algotrading/comments/1t1hpq4/_/ojkqpx3/)

> ...ied scraping everything live and got rate limited into oblivion haha. now i usually just dump everything into clickhouse cuz csv files get messy rly quick once u start doing multi-timeframe stuff. this looks solid tho th...  
> [score 10](https://www.reddit.com/r/algotrading/comments/1qncdrx/_/o1w0138/)

> clickhouse is over-engineering...  
> [score 6](https://www.reddit.com/r/algotrading/comments/1p4sb7p/_/nqen3y8/)

> ...like 90% data eng at the start but u might be over-engineering the db part early on. i moved from postgres to clickhouse for time-series data and it saved me so much headache with scaling those hundreds of millions of ro...  
> [score 6](https://www.reddit.com/r/algotrading/comments/1qyohsj/_/o46a0qx/)

> Databento for data  Wedbush for execution  Rust, Python custom platform  Clickhouse, Parquet, DuckDB, Jupyter for historical and and research...  
> [score 6](https://www.reddit.com/r/algotrading/comments/1tlx366/_/onivbaq/)

> ...pps, CLI apps, Analysis (buckets, opportunity, scoring, fitness, etc), CUDA (brute forcing parameters)..  DB: clickhouse for tick data. MSSQL for everything else.  tick data is also stored as delta compressed archives so...  
> [score 5](https://www.reddit.com/r/algotrading/comments/1u0i56x/_/oqizemk/)

> ...*  Python: Analysis/Research/Modelling *  L1 data storage in custom format on disk *  Mongo: Model storage *  ClickHouse: bars, features, research and model output database *  2 QuantVPS in Chicago (Paper/Live) *  NATS *...  
> [score 5](https://www.reddit.com/r/algotrading/comments/1u9xae8/_/oskvhyg/)

> ...'m over-engineering, but for the size of backtests I need to run/output I don't believe I am. if i was to use clickhouse why not just use duckdb? everything is being run locally...  
> [score 4](https://www.reddit.com/r/algotrading/comments/1p4sb7p/_/nqdzq7r/)

> ...+ is a massive trap unless ur latency sensitive during the backtest itself. i've always gone hybrid—python or clickhouse for the heavy lifting and research, then porting the logic to the execution engine once the strateg...  
> [score 4](https://www.reddit.com/r/algotrading/comments/1s7vvc6/_/odcrllv/)

> ...that subscribes to contracts, pushes data it to NATS and a local sqlite DB. after 7 days, the sqlite dumps to clickhouse server at home.  * container(s) that run strategie(s) that listen to NATS for trades and porfolio/o...  
> [score 4](https://www.reddit.com/r/algotrading/comments/1vhwu16/_/p2973ob/)

> Start simple. Daily bars in parquet partitioned by symbol and date. Need tick data later? QuestDB or ClickHouse handle it well. Match storage to your access pattern. If queries are symbol X from date A to B, flat files w...  
> [score 3](https://www.reddit.com/r/algotrading/comments/1tzpk3p/_/oqfl43e/)

> why tailscale and not clickhouse or some other columnar DB?  or influxdb (iox) since you're on rust?...  
> [score 2](https://www.reddit.com/r/algotrading/comments/1qklj4o/_/o1akhya/)

> ...limits rly suck when ur trying to pull years of history at once. tbh once u have the files just dump them in clickhouse or smth to make that seasonal analysis faster....  
> [score 2](https://www.reddit.com/r/algotrading/comments/1r320ev/_/o5ce7k8/)

> This is a cool stack. ClickHouse + Centrifugo + lightweight-charts is a pretty sane combo for this kind of app.  Tiny unsolicited note from chart-rendering land: if you ever hit limits with dense candles/equity curves or...  
> [score 2](https://www.reddit.com/r/algotrading/comments/1t1hpq4/_/ookxy17/)

> ...each these volumes the architecture is scalable and allows for growth.  Read the 'Three-Tier OLAP Approach' + ClickHouse paragraphs.  from the documentation.  [https://datapallas.com/docs/bi-analytics/data-warehouse-olap...  
> [score 2](https://www.reddit.com/r/algotrading/comments/1td3ah3/_/omapwer/)

> been there done that.. got like TBs of tick data in clickhouse.   databento, polygon, esignals .. some random archive off a website.  then IBKR and eventually alpaca.  but then after years, i realized.. data is just a me...  
> [score 2](https://www.reddit.com/r/algotrading/comments/1tw23l4/_/opog7jr/)

> ...ple to bars, write parquet, and every backtest after that reads the parquet. sqlite would fall over on it and clickhouse is more ops than a single research box needs.  one thing worth being clear on, the 315 was the trad...  
> [score 2](https://www.reddit.com/r/algotrading/comments/1vdsc8o/_/p1fnugj/)

> clickhouse is for large amounts of data you want to archive (limited deletion/modifications). it structures and compresses by column using delta/zigzag, etc.. instead of by row.   so instead of storing price as: 101,102,...  
> [score 2](https://www.reddit.com/r/algotrading/comments/1vhwu16/_/p2sek58/)

> ...end up with multiple copies of the same data for speed and convenience on what you do with it.   I have it in clickhouse to derive time bars &  MAs, parquet files for archive/backup, a local compressed format for quick l...  
> [score 2](https://www.reddit.com/r/algotrading/comments/1w6r0g6/_/p7qkzte/)

> ...up writing your own universe logic and data pipeline. What’s helped me is keeping data/metrics in Postgres or ClickHouse, running scans there, then feeding candidates into the engine; I’ve wired that with Lean/Backtrader...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1pydn9s/_/nwiryc2/)

