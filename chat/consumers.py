import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.utils import timezone


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.id = self.scope["url_route"]["kwargs"]["course_id"]
        self.user = self.scope["user"]
        self.room_group_name = "chat_%s" % self.id
        # join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    # receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        now = timezone.now()
        # send message to room group
        await self.channel_layer.group_senda(
            self.room_group_name,
            {
                "type": "chat_message",
                "message": message,
                "user": self.user.username,
                "time": now.strftime("%H:%M:%S"),
            },
        )

    # receive message from room group
    async def chat_message(self, event):
        # Send message to WebSocket
        await self.send(text_data=json.dumps(event))
