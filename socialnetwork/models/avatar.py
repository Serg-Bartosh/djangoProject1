from django.db import models
from django.utils.text import slugify

from djangoProject1.settings import MEDIA_ROOT
from socialnetwork.models import User


def file_location(instance, filename):
    username = instance.user.username
    safe_username = slugify(username)
    file_path = f"avatar/{safe_username}_{filename}"
    return file_path


class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=file_location, null=False, blank=True)
