import json 
import asyncio
import aiohttp
import yfinance as yf
from channels.generic.websocket import AsyncWebsocketConsumer
class StockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.task = asyncio.create_task(self.send_data())

    async def disconnect(self, code):
        return await super().disconnect(code)
    
    async def send_data(self):
        await asyncio.sleep(0.1)
        stock = await self.stock_market_live_data()
        if stock:
            await self.send(json.dumps(stock))
        self.task = asyncio.create_task(self.send_data())
    

    async def stock_market_live_data(self):
        tickers = ["AAPL", "GOOGL", "MSFT", "TSLA"]
        data = await asyncio.to_thread(yf.download,tickers,period="1d",interval='1m')
        
        stock_data = []
        for ticker in tickers:
            stock_data.append(
                {
                    'stock_name':ticker,
                    'Open_price':float(data['Open'][ticker].iloc[-1]),
                    'Close_price':float(data['Close'][ticker].iloc[-1]),
                    'High_price':float(data['High'][ticker].iloc[-1]),
                    'Low_price':float(data['Low'][ticker].iloc[-1])               
                }
            )
        return stock_data