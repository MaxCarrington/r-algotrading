# QuantStats

Mentioned 14 times across 10 threads. [Back to index](../README.md)

**Often discussed with:** [US equities](../asset_classes/us-equities.md) (9), [Python](../tools/python.md) (8), [Futures](../asset_classes/futures.md) (6), [Options](../asset_classes/options.md) (5), [TradingView / Pine Script](../tools/tradingview-pine-script.md) (5), [Crypto](../asset_classes/crypto.md) (3), [Forex](../asset_classes/forex.md) (3), [Breakout / ORB](../strategy_families/breakout-orb.md) (3), [Machine learning](../strategy_families/machine-learning.md) (3), [Momentum](../strategy_families/momentum.md) (3), [Order flow / microstructure](../strategy_families/order-flow-microstructure.md) (3), [Portfolio / allocation](../strategy_families/portfolio-allocation.md) (3)

## Top threads

- [2 years building, 3 months live: my mean reversion + ML filter strategy breakdown](https://www.reddit.com/r/algotrading/comments/1pnzf9l/) · 2025-12-16 · score 125 · 1 comments
- [Diversified multi-strategy portfolio](https://www.reddit.com/r/algotrading/comments/1r1gwo6/) · 2026-02-10 · score 98 · 1 comments
- [Crisis protected portfolio](https://www.reddit.com/r/algotrading/comments/1pjkmzv/) · 2025-12-11 · score 88 · 1 comments
- [A real professional backtest is walk-forward analysis. Anything else is an illusion.](https://www.reddit.com/r/algotrading/comments/1t5e9q6/) · 2026-05-06 · score 30 · 1 comments
- [Blue is performance of my forex bots, orange is performance of my indices bot, would it make sense to look into scaling their risk up or down depending on their performance over an x number of days?](https://www.reddit.com/r/algotrading/comments/1p4sqte/) · 2025-11-23 · score 23 · 2 comments
- [Where do you backtest your strategies](https://www.reddit.com/r/algotrading/comments/1vtwj32/) · 2026-08-20 · score 22 · 2 comments
- [Any genuinely free backtesting tools?](https://www.reddit.com/r/algotrading/comments/1tiqq1x/) · 2026-05-20 · score 16 · 2 comments
- [What do you use to visualise your strategies?](https://www.reddit.com/r/algotrading/comments/1p3wjke/) · 2025-11-22 · score 5 · 1 comments
- [Quant Analyzer is Dope](https://www.reddit.com/r/algotrading/comments/1ssm19h/) · 2026-04-22 · score 0 · 2 comments
- [Anyone knows how to sort Multicharts backtesting results using Sharpe ratio?](https://www.reddit.com/r/algotrading/comments/1vf3ow7/) · 2026-08-04 · score 0 · 1 comments

## What people said

> ...for initial idea validation, Nautilus for official validation and live engine. [https://github.com/ranaroussi/quantstats](https://github.com/ranaroussi/quantstats) for advanced metrics (including my own custom dashboard...  
> [score 5](https://www.reddit.com/r/algotrading/comments/1vtwj32/_/p4x9bv1/)

> ...version also makes money (or breaks even), your ML isn't doing anything.  I haven't tried but Python wrapper `quantstats` seems pretty cool. It should calculate correct Sharpe, underwater plot and your correlation with B...  
> [score 3](https://www.reddit.com/r/algotrading/comments/1pnzf9l/_/nucutsp/)

> Just do not pay for it. The free version is very limited. You can get same stats with Python and Quantstats etc....  
> [score 3](https://www.reddit.com/r/algotrading/comments/1ssm19h/_/ohn32ig/)

> ...at was my point - not what you split it into) but the nuance of your point may be lost on me.  I’ll look into quantstats and pyfolio thanks. I still maintain say 30% equity on the line with 1%risk per trade for a bot inv...  
> [score 2](https://www.reddit.com/r/algotrading/comments/1p4sqte/_/nqlyocq/)

> Rust, I use the chapaty library. It's a solid backtesting framwork, outputs QuantStats tear sheets out of the box and has built in grid searches. There is a template repo you can use with a running example. It provides c...  
> [score 2](https://www.reddit.com/r/algotrading/comments/1vtwj32/_/p4z7330/)

> ...lise it on a chart. What do you use for it?  For exploring ideas, nothing beats pandas, matplotlib (and maybe quantstats/pyfolio/zipline) in a jupyter environment.  If you want a front-end that's prettier, you can very e...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1p3wjke/_/nq8rapx/)

> ...re a beginner and not profitable yet, I'd recommend you to check out the basic trading system metrics through quantstats and pyfolio.  They aren't perfect but they do provide a good starting point for judging whether an...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1p4sqte/_/nqluao3/)

> Quantstats...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1pjkmzv/_/ntipueu/)

> I had to code my own, but yes it's in python. Some parts use existing libraries, like exchange calendars, quantstats, etc....  
> [score 1](https://www.reddit.com/r/algotrading/comments/1r1gwo6/_/o4riue5/)

> quantstats in python does like 90% of what quant analyzer does and its free. monte carlo reshuffle of trade sequences is 20 lines of code too. if youre already running backtests in python adding the stats layer is cheape...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1ssm19h/_/ohnkb0m/)

> ...:  oos = \[run\_strategy(test) for train, test in walk\_forward(540, 30)\]  equity = pd.concat(oos).cumsum()  quantstats and vectorbt ship this out of the box. the fragmented look people post is usually train+test plotte...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1t5e9q6/_/okas935/)

> ...you load and it handles everything from order execution, matching engine, data sync, and reporting (including quantstats tearsheet)  The loop is: call reset -> agent acts on the initial observation -> environment advance...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1tiqq1x/_/ondwlyh/)

> That gym-style pattern maps well to real execution, and quantstats + CSV output is a good foundation. The real challenge I've seen most teams face moving to live is usually in the environment model itself - slippage, par...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1tiqq1x/_/onhmyji/)

> For my Sharpe Ratio I normalize to end of day PnL and then let quantstats compute it...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1vf3ow7/_/p1ly0sr/)

