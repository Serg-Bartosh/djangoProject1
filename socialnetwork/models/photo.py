from django.db import models

from socialnetwork.models import User


def file_location(instance, filename):
    username = instance.user.username
    file_path = f"photo/{username}_{filename}"
    return file_path


class Photo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=file_location, null=False, blank=True)
