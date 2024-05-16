from django.db import models


# TODO: Поменять способы сохранения сообщений:
#  Добавить привязку юзеров к чату, создание груп

class Chat(models.Model):
    room_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
