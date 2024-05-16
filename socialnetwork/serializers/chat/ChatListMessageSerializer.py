from rest_framework import serializers

from socialnetwork.models import User
from socialnetwork.models.chat.message import ChatMessage


class MessageListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = ChatMessage
        fields = ['author', 'content', 'created_at']

    def get_author(self, obj):
        author_obj = User.objects.get(pk=obj.author_id)
        return author_obj.username
