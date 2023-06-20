# myapp/consumers.py

import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer
from asgiref.sync import async_to_sync
from main.models import *


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        # Called when a new WebSocket connection is established.
        self.room_group_name = 'test'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        
        self.accept()

        messages = BotInteraction.objects.prefetch_related()
        data = []
        count = {}
        for msg in messages:
            data.append({'user_id': msg.user.user_id, 'username': msg.user.username, 'first_name': msg.user.first_name, 'last_name': msg.user.last_name, 'user_choice': msg.message, 'joke': msg.response })

            if msg.user.user_id not in count:
                count[msg.user.user_id] = 1
            else:
                count[msg.user.user_id] += 1

        c = []
        for k,v in count.items():
            c.append({'user_id': k, 'c': v})

        self.send(text_data = json.dumps({
            'type': 'connection_established',
            'data': data,
            'c': c,
        }))

    # def disconnect(self, close_code):
    #     # Called when the WebSocket connection is closed.
    #     pass

    def receive(self, text_data):
        # Called when a message is received from the WebSocket.
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, 
            {
                'type': 'chat_message',
                'message': message
            }
        )

    def chat_message(self, event):
        message = event['message']
        self.send(text_data=json.dumps({'type': 'chat', 'message': message}))