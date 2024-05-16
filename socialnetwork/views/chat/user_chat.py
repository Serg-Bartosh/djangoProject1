from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ViewSet

from socialnetwork.models import User, Avatar, ChatMessage
from socialnetwork.models.chat.chat import Chat


class UserChatViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def get_recipient(self, user_id, chats):
        result_other_user_data = []
        # TODO: serializer
        for chat in chats:
            usernames = sorted(chat.room_name.split('_'))
            other_username = usernames[0] if usernames[0] != user_id else usernames[1]
            other_user = User.objects.get(pk=other_username)
            count_new_messages = ChatMessage.objects.filter(chat_id=chat.id, author=other_user.id, state="NEW").count()
            try:
                other_user_image = Avatar.objects.get(pk=other_user.id)
            except Avatar.DoesNotExist:
                other_user_data = {
                    'image': None,
                    'username': other_user.username,
                    'id': other_user.id,
                    'new_messages': count_new_messages
                }
                result_other_user_data.append(other_user_data)
                continue

            other_user_data = {
                'image': other_user_image.image,
                'username': other_user.username,
                'id': other_user.id,
                'new_messages': count_new_messages
            }
            result_other_user_data.append(other_user_data)
        return result_other_user_data

    def list(self, request):
        user_id = request.user.id
        chats = Chat.objects.filter(room_name__icontains=user_id).all()
        recipient_data = self.get_recipient(str(user_id), chats)
        context = {
            'recipients': recipient_data
        }
        return render(request, context=context, template_name='templates/chat/user_chat.html')
