# CoinGecko / CoinMarketCap

Mentioned 16 times across 15 threads. [Back to index](../README.md)

**Often discussed with:** [Crypto](../asset_classes/crypto.md) (14), [US equities](../asset_classes/us-equities.md) (8), [Binance](../brokers/binance.md) (7), [Options](../asset_classes/options.md) (5), [Order flow / microstructure](../strategy_families/order-flow-microstructure.md) (5), [Python](../tools/python.md) (5), [Futures](../asset_classes/futures.md) (4), [ETFs](../asset_classes/etfs.md) (3), [Prediction markets](../asset_classes/prediction-markets.md) (3), [Alpaca](../brokers/alpaca.md) (3), [Alpaca (data)](../data_sources/alpaca-data.md) (3), [Arbitrage](../strategy_families/arbitrage.md) (3)

## Top threads

- [I built a bot to automate 'risk-free' arbitrage between Kalshi and Polymarket. Here is the source code.](https://www.reddit.com/r/algotrading/comments/1qebxud/) · 2026-01-16 · score 281 · 2 comments
- [Built a multi-asset algo trading bot from scratch. 4 weeks of paper trading, thinking about going live.](https://www.reddit.com/r/algotrading/comments/1tdeu7b/) · 2026-05-14 · score 112 · 1 comments
- [An amazing quote by Jim Simons that every trader should see](https://www.reddit.com/r/algotrading/comments/1ttvzrr/) · 2026-06-01 · score 105 · 1 comments
- [What API feeds do you rely on?](https://www.reddit.com/r/algotrading/comments/1tlx366/) · 2026-05-24 · score 21 · 1 comments
- [Integrating a Crypto WebSocket API for 1-second onchain OHLCV - Architecture tips?](https://www.reddit.com/r/algotrading/comments/1ptxwoj/) · 2025-12-23 · score 4 · in post
- [Best free real-time crypto WebSocket options for algo trading right now?](https://www.reddit.com/r/algotrading/comments/1t149df/) · 2026-05-01 · score 3 · in post
- [historical Polymarket orderbook data recommendation](https://www.reddit.com/r/algotrading/comments/1tidjik/) · 2026-05-20 · score 5 · 1 comments
- [One thing I wish I knew before building a Crypto Trading Bot API setup](https://www.reddit.com/r/algotrading/comments/1t89qgm/) · 2026-05-09 · score 2 · in post
- [historical Crypto market data recommedation](https://www.reddit.com/r/algotrading/comments/1tke39i/) · 2026-05-22 · score 4 · 1 comments
- [Finally found a Free Crypto API that actually covers everything](https://www.reddit.com/r/algotrading/comments/1t0z8t1/) · 2026-05-01 · score 1 · in post
- [If you're using a Free Crypto API for a side project, don’t ignore global market metrics](https://www.reddit.com/r/algotrading/comments/1tb4ssu/) · 2026-05-12 · score 1 · in post
- [API for delayed stock/crypto/metals prices (portfolio tracking app)](https://www.reddit.com/r/algotrading/comments/1qvwiji/) · 2026-02-04 · score 1 · 1 comments
- [Started backtesting crypto strategies using CMC's historical data, here's what I found](https://www.reddit.com/r/algotrading/comments/1sd921x/) · 2026-04-05 · score 0 · in post
- [How much historical crypto data do you need before a backtest is worth trusting?](https://www.reddit.com/r/algotrading/comments/1u2x2mj/) · 2026-06-11 · score 0 · in post
- [Most crypto spread signals are garbage until you model execution properly](https://www.reddit.com/r/algotrading/comments/1u2x3uz/) · 2026-06-11 · score 0 · in post

## What people said

> ...ay from REST polling and fully embrace a crypto websocket API for real-time signals.  I've decided to go with CoinGecko's [WebSocket API](https://docs.coingecko.com/websocket) because they have 1-second onchain OHLCV upd...  
> [score 4](https://www.reddit.com/r/algotrading/comments/1ptxwoj/)

> ...nified REST, but the free WebSocket support is pretty limited. Not great for true low-latency strategies. * **CoinGecko / CoinMarketCap**: Easy and generous free tiers, but mostly delayed REST calls. Their WebSocket opti...  
> [score 3](https://www.reddit.com/r/algotrading/comments/1t149df/)

> ...nsus" price, which is just the average price across trading. Prices across platforms differ; aggregators like CoinGecko get you the most accurate price....  
> [score 2](https://www.reddit.com/r/algotrading/comments/1qebxud/_/nzxbdqz/)

> ...ure for historical candles  proper retry logic  handling rate limits early  I moved a lot of my inputs to the CoinMarketCap API because it was easier than stitching together multiple random sources.  Especially for backt...  
> [score 2](https://www.reddit.com/r/algotrading/comments/1t89qgm/)

> Didn’t know this. So, to dumb it down (for me). If CoinGecko shows that the BTC price is falling, the price on PolyMarket will follow and go down aswel?  But isn’t it a matter of milliseconds? So how would the bot benefi...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1qebxud/_/nzxfibn/)

> For crypto specifically, give Coingecko's API a go. They have a free demo plan that covers a lot - price data, historical prices, market data, coin metadata. Should be more than enough if you're working with delayed data...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1qvwiji/_/o70c8ck/)

> ...uff), and I kept running into the same issue — either limited data or weird gaps.  Recently started using the CoinMarketCap API and it’s honestly way more complete than I expected.  You can pull:  live prices + market ca...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1t0z8t1/)

> ...ypto market cap BTC dominance 24h market volume Fear & Greed style sentiment indicators   I started using the CoinMarketCap API for this and it gave much better context than watching random charts.   Example:   If your p...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1tb4ssu/)

> Not currently, the sentiment pipeline is NewsAPI headlines + Reddit + CoinGecko Fear & Greed as inputs fed to Claude for scoring. Unusual Whales would be interesting for options flow but there are no options in the bot r...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1tdeu7b/_/omcquul/)

> ...ook, polymarket api has historical trades. for full orderbook reconstruction youll need third party data like coingecko or the chain itself. l2 reconstruction from chain takes work...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1tidjik/_/or8n21u/)

> CoinMarketCap API is worth comparing here if you mainly need broad historical market data rather than raw tick/order book depth. It has historical pricing plus Binance/Kraken exchange data, so it may be a more practical...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1tke39i/_/oupeckq/)

> ...ith their broker’s feed, but once they need broader market coverage they usually look at dedicated providers. CoinMarketCap API gets mentioned quite a bit because it combines market data, exchange data, historical pricin...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1tlx366/_/ouav39w/)

> ...arket my algo executes.  I mean I would not add coinbase data if the execution is on binance. I would not use coinmarketcap's data because it is an aggregator so it dismisses too much data and it lags. And I would not us...  
> [score 1](https://www.reddit.com/r/algotrading/comments/1ttvzrr/_/op6gb4c/)

> ...trading lately and one of the hardest parts was finding reliable historical crypto data. I started using the CoinMarketCap API and honestly the data quality is really solid.  They've got OHLCV data, going all the way ba...  
> [score 0](https://www.reddit.com/r/algotrading/comments/1sd921x/)

> ...see how the same logic behaved across older cycles, so I started pulling longer historical OHLCV data through CoinMarketCap’s API and storing it locally before running tests.      The setup is basic:      Pull historical...  
> [score 0](https://www.reddit.com/r/algotrading/comments/1u2x2mj/)

> ...elped was splitting the data into two layers instead of pretending one feed can answer everything.      I use CoinMarketCap’s API more as a broad reference layer for market price, volume, and exchange context. Then anyth...  
> [score 0](https://www.reddit.com/r/algotrading/comments/1u2x3uz/)

