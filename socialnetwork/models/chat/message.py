from django.db import models
from rest_framework.authtoken.admin import User

from socialnetwork.models.chat.chat import Chat


class ChatMessage(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    content = models.CharField(max_length=256, blank=True)
    state = models.CharField(default="NEW", max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
