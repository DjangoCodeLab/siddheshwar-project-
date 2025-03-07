import json
import asyncio
import aiohttp
from channels.generic.websocket import AsyncWebsocketConsumer

class StockConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.task = asyncio.create_task(self.send_photos())

    async def disconnect(self, code):
        return await super().disconnect(code)
    
    async def send_photos(self):
        await asyncio.sleep(4)
        image  = await self.get_data()
        if image:
            await self.send(json.dumps(image))
        self.task = asyncio.create_task(self.send_photos())
        


    async def get_data(self):
        url = "https://dog.ceo/api/breeds/image/random"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json() 
                    return data.get('message')