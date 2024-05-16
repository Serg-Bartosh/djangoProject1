from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet

from socialnetwork.models.chat.chat import Chat
from socialnetwork.models.chat.message import ChatMessage
from socialnetwork.serializers.chat.ChatListMessageSerializer import MessageListSerializer
from socialnetwork.utilities.chat.change_state_message import change_state_message


class ChatViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request, user_id):
        # TODO: переименовать user_id
        # TODO: Проверка на отправку сообщений самому себе
        user = request.user
        room_name = f'{min(user_id, user.id)}_{max(user_id, user.id)}'
        try:
            chat = Chat.objects.get(room_name=room_name)
        except Chat.DoesNotExist:
            return render(request, 'templates/chat/chat.html', context={'user_id': user_id})
        change_state_message(chat, user)
        messages = ChatMessage.objects.filter(chat_id=chat.id).all()
        serializer = MessageListSerializer(messages, many=True)
        context = {'user_id': user_id, 'messages': serializer.data}
        return render(request, 'templates/chat/chat.html', context=context)
