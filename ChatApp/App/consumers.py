from channels.generic.websocket import AsyncWebsocketConsumer
import json
class ChatConsumer(AsyncWebsocketConsumer):
    users = {}
    async def connect(self):
        await self.accept()
        self.username = None 

    async def disconnect(self,close_code):
        if self.username:
            del self.users[self.channel_name]
            await self.channel_layer.group_send(
                'chatroom',
                {
                    "type": "user_list",
                    "user":list(self.users.values())
                }
            )

    async def receive(self, text_data):
        data = json.loads(text_data)

        if "username" in data:
            self.username = data["username"]
            self.users[self.channel_name] = self.username
            await self.channel_layer.group_add("chatroom",self.channel_name)
            await self.channel_layer.group_send("chatroom",{
                "type":"user_list",
                "users":list(self.users.values())
            })

        elif "message" in data:
            await self.channel_layer.group_send("chatroom",{"type":"chat_message","user":self.username,"message":data["message"]})

        
    async def chat_message(self,event):
        await self.send(
            text_data = json.dumps({
                "user":event["user"],
                "message":event["message"]
            })
        )

    async def user_list(self,event):
        await self.send(
            text_data = json.dumps({
                "users":event["users"]
            })
        )