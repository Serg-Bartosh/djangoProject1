from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer
import json

from django.utils import timezone

from socialnetwork.models import Chat, ChatMessage


class ChatConsumer(JsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = None
        self.other_user_id = None
        self.chat = None
        self.room_name = None

    def is_write_to_yourself(self):
        if self.user == self.other_user_id:
            self.close()

    # TODO: проверка на то что бы юзер не писал сам себе
    def create_room_name(self):
        user_id = self.user.id
        if user_id and self.other_user_id:
            room_name = f'{min(user_id, self.other_user_id)}_{max(user_id, self.other_user_id)}'
            self.room_name = room_name
        else:
            raise ValueError("Invalid user or user_id")

    def connect(self):
        self.user = self.scope["user"]
        self.other_user_id = self.scope["url_route"]['kwargs']["user_id"]
        self.is_write_to_yourself()
        self.accept()
        self.create_room_name()
        self.chat, _ = Chat.objects.get_or_create(room_name=self.room_name)
        async_to_sync(self.channel_layer.group_add)(
            self.room_name,
            self.channel_name,
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_name,
            self.channel_name,
        )
        self.close()

    def receive(self, text_data):
        data = json.loads(text_data)
        message = data.get('message')
        timestamp = timezone.now().isoformat()
        if message:
            message_obj = ChatMessage.objects.create(author=self.user, chat=self.chat, content=message)
            async_to_sync(self.channel_layer.group_send)(
                self.room_name,
                {
                    'type': 'chat.message',
                    "author": self.user.username,
                    'content_id': message_obj.id,
                    'content': message,
                    'timestamp': timestamp
                },
            )

    def chat_message(self, event):
        self.send_json(event)
