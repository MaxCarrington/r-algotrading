# ib_insync / ib_async

Mentioned 29 times across 20 threads. [Back to index](../README.md)

**Often discussed with:** [Interactive Brokers](../brokers/interactive-brokers.md) (19), [Python](../tools/python.md) (18), [Options](../asset_classes/options.md) (13), [US equities](../asset_classes/us-equities.md) (12), [Alpaca](../brokers/alpaca.md) (12), [Alpaca (data)](../data_sources/alpaca-data.md) (12), [Futures](../asset_classes/futures.md) (10), [Order flow / microstructure](../strategy_families/order-flow-microstructure.md) (10), [TradingView / Pine Script](../tools/tradingview-pine-script.md) (9), [Crypto](../asset_classes/crypto.md) (8), [Schwab / TD Ameritrade](../brokers/schwab-td-ameritrade.md) (8), [Claude](../tools/claude.md) (8)

## Top threads

- [I reverse-engineered the IB Gateway and rebuilt it in Rust for low latency](https://www.reddit.com/r/algotrading/comments/1rveu7e/) · 2026-03-16 · score 177 · 3 comments
- [Quite fed up with the piece of garbage called IB api](https://www.reddit.com/r/algotrading/comments/1w0adbu/) · 2026-08-27 · score 52 · 1 comments
- [IBKR API is a fucking joke!](https://www.reddit.com/r/algotrading/comments/1t7ashk/) · 2026-05-08 · score 40 · 3 comments
- [More Results of my BTC/EUR Algo Trading](https://www.reddit.com/r/algotrading/comments/1ouz38t/) · 2025-11-12 · score 36 · 1 comments
- [Have a winning strategy](https://www.reddit.com/r/algotrading/comments/1oe95h2/) · 2025-10-23 · score 33 · 2 comments
- [I am a programmer who has been trading for almost a year, I have no idea where to start with algotrading](https://www.reddit.com/r/algotrading/comments/1tby5um/) · 2026-05-13 · score 27 · 2 comments
- [Has anyone tried using AI agents for execution?](https://www.reddit.com/r/algotrading/comments/1tmwzpy/) · 2026-05-25 · score 23 · 1 comments
- [Moving my manual options strategy to a bot (5-10 trades per day). Need API advice.](https://www.reddit.com/r/algotrading/comments/1ri6w1f/) · 2026-03-01 · score 21 · 2 comments
- [Which broker are you using for US equities algo trading and why?](https://www.reddit.com/r/algotrading/comments/1ohsiig/) · 2025-10-27 · score 15 · 1 comments
- [For those who use IBKR as their broker, how do you use their data in your setup? If not, why?](https://www.reddit.com/r/algotrading/comments/1wf7at8/) · 2026-09-13 · score 14 · 2 comments
- [Which Broker To Use?](https://www.reddit.com/r/algotrading/comments/1sbxmy7/) · 2026-04-04 · score 13 · 2 comments
- [What do algotraders need?](https://www.reddit.com/r/algotrading/comments/1rtqogp/) · 2026-03-14 · score 13 · 1 comments
- [What platform is the best for someone just starting?](https://www.reddit.com/r/algotrading/comments/1s4ltwz/) · 2026-03-26 · score 8 · 1 comments
- [Tools setup help](https://www.reddit.com/r/algotrading/comments/1okho3n/) · 2025-10-31 · score 5 · 1 comments
- [Broker APIs and AI-assisted trading setups accessible from Norway?](https://www.reddit.com/r/algotrading/comments/1x5rvtr/) · 2026-10-14 · score 5 · 1 comments
- [Calling Canadian Traders](https://www.reddit.com/r/algotrading/comments/1sbq96j/) · 2026-04-03 · score 3 · 1 comments
- [API](https://www.reddit.com/r/algotrading/comments/1t1y3s7/) · 2026-05-02 · score 2 · 1 comments
- [Broker choice for Europe](https://www.reddit.com/r/algotrading/comments/1tbydmq/) · 2026-05-13 · score 1 · 1 comments
- [No fractional share via the shitty IB api?](https://www.reddit.com/r/algotrading/comments/1x20axx/) · 2026-10-09 · score 1 · 1 comments
- [Centralized bot that sends signals to brokers using their API](https://www.reddit.com/r/algotrading/comments/1vbhhe0/) · 2026-07-31 · score 0 · 1 comments

## What people said

> The ib_async library that's used for IB is also open source, if we're using that, why wouldn't we use this?...  
> [score 23](https://www.reddit.com/r/algotrading/comments/1rveu7e/_/oasillx/)

> ...ding. is the way to go.  Mature software, plethora of libraries. Orchestrate via ibcAlpha and with Python and ib_async. Nothing better out there....  
> [score 15](https://www.reddit.com/r/algotrading/comments/1t7ashk/_/okok8vz/)

> Jay-Dirt absolutely nailed the IBKR headless setup. TWS is a resource nightmare, but IB Gateway + IBC + `ib_insync` is the industry standard for a 'set and forget' Python stack.  Coming at this from a full-stack dev pers...  
> [score 11](https://www.reddit.com/r/algotrading/comments/1sbxmy7/_/oea4zi6/)

> ...is "IB Gateway"  https://www.interactivebrokers.com/en/trading/ibgateway-latest.php  works fine for me (using ib_async python library), but I have it managed by IBC  https://github.com/IbcAlpha/IBC...  
> [score 9](https://www.reddit.com/r/algotrading/comments/1t7ashk/_/okny8yg/)

> ...e you catch the cases where the model hallucinates a strike that doesn't exist or sizes 5x too big. IBKR has `ib_insync` and Alpaca has a clean REST API, both take a weekend to wire up.       The LLM-direct-to-broker pat...  
> [score 8](https://www.reddit.com/r/algotrading/comments/1tmwzpy/_/onqxo03/)

> I multi-broker-connector.   I think, many of us use something like ib_async and it would be nice to have a solution that supports multiple brokers, without having to code it. Could be a nice community-project....  
> [score 7](https://www.reddit.com/r/algotrading/comments/1rtqogp/_/oag12j7/)

> ...paste code.  Start there: • Learn Python well, not Java (IB has brutal official and community libraries like ib_insync). • Create a local database to save historical data, not relying only on TradingView. • Separate res...  
> [score 6](https://www.reddit.com/r/algotrading/comments/1oe95h2/_/nl0984g/)

> ...Run IB Gateway. It's their stripped-down version meant purely for API connections. It will save your RAM. 2.	ib_insync: Since you're using Python in VS Code, definitely check out the ib_insync library. It makes the nati...  
> [score 6](https://www.reddit.com/r/algotrading/comments/1sbxmy7/_/oe92g6e/)

> ...gView alerts to a tiny webhook that fires orders. Keep it simple first, then harden.  IBKR: use IB Gateway + `ib_insync` on your Mac. TWS works but Gateway is cleaner for headless. 100–300 ms is fine unless you’re trying...  
> [score 5](https://www.reddit.com/r/algotrading/comments/1okho3n/_/nmdqq6g/)

> ...papertrading set up on ibkr.  > There are https://github.com/deepentropy/ibx/tree/main/notebooks adapted from ib_async's examples covering basics, market data, historical bars, tick-by-tick, and ordering.  That link does...  
> [score 5](https://www.reddit.com/r/algotrading/comments/1rveu7e/_/oatd06a/)

> ...aude.ai - I am using IBC with IB Gateway to algotrade in my IBKR account.  Please write python code using the ib_async library to sign into my account and buy 10 shares of QQQ with a limit price 0.10 below the current ma...  
> [score 5](https://www.reddit.com/r/algotrading/comments/1tby5um/_/ollfvml/)

> IBKR with the ib_async python library. Been using them for manual trading and documentation was good enough to move to algo trading without friction....  
> [score 3](https://www.reddit.com/r/algotrading/comments/1ohsiig/_/nls36pv/)

> Interactive brokers - ib_async...  
> [score 3](https://www.reddit.com/r/algotrading/comments/1ri6w1f/_/o860n04/)

> Gemini cli can do it as well if you know what you need and can articulate.  Python with ib_async that's how I did it. But you need to run the TWS all the time to connect through the TWS API to IBKR. That's where it gets...  
> [score 2](https://www.reddit.com/r/algotrading/comments/1oe95h2/_/nl3twyp/)

> ...5m data every 1-2 minutes, and calculate the 9EMA yourself.  Claude.ai can easily write the python code using ib_async (ibkr) or schwab-py (schwab)...  
> [score 2](https://www.reddit.com/r/algotrading/comments/1ri6w1f/_/o86gx1f/)

> ...have around 500ms to have a limit order submitted, so that seems accurate from my experience. I use python's ib_async to interact with IB Gateway...  
> [score 2](https://www.reddit.com/r/algotrading/comments/1rveu7e/_/oasekhc/)

> ...a PyTorch engine for daily swing trades and wrestling with their headless Gateway setup. I am using Xvfb and ib_insync to bypass their UI entirely and just run it in the background. It is a grind to set up, but it beats...  
> [score 2](https://www.reddit.com/r/algotrading/comments/1sbq96j/_/oe93wed/)

> ...andard for EU algo because of API depth + low fees + multi-asset coverage. they have an official java sdk and ib_async (python) but the underlying protocol works with any language. for kotlin specifically you can call ib...  
> [score 2](https://www.reddit.com/r/algotrading/comments/1tbydmq/_/olq64gm/)

> ...t on 1m/5s bars, include spread/slippage, and do walk‑forward; only pay for depth once live.   For execution: ib_insync for IBKR, CCXT for crypto, and a simple risk layer (position caps, max daily loss, circuit breaker)....  
> [score 1](https://www.reddit.com/r/algotrading/comments/1ouz38t/_/npe4a0z/)

> ...oud infrastructure and don't want to manage data feeds yourself.  For live execution: **Interactive Brokers + ib_insync** is the battle-tested path. Not the prettiest API but it works and has serious options support.  On...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1s4ltwz/_/od9zbqr/)

