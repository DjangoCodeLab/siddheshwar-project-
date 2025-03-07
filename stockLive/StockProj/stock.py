import json 
import asyncio
import yfinance as yf

async def stock_market_live_data():
    tickers = ["AAPL", "GOOGL", "MSFT", "TSLA"]
    stock_data = []
    for ticker in tickers:
        data = await asyncio.to_thread(yf.Ticker(ticker).history,period="1d",interval='1m')
        stock_data.append(
            {
                'stock_name':ticker,
                'Open_price':float(data['Open'].iloc[-1]),
                'Close_price':float(data['Close'].iloc[-1]),
                'High_price':float(data['High'].iloc[-1]),
                'Low_price':float(data['Low'].iloc[-1])               
             }
        )
    print(stock_data)

asyncio.run(stock_market_live_data())