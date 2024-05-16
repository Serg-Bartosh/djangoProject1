import random

from django.core.validators import validate_image_file_extension
from django.db import models

from socialnetwork.models import User


def file_location(instance, filename):
    username = instance.author.username
    file_path = f"article/{username}-{instance.title}-{filename}"
    return file_path


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField(max_length=5000, null=False, blank=False)
    image = models.ImageField(upload_to=file_location, null=False, blank=True,
                              max_length=1048576,  # 1 Bite
                              validators=[validate_image_file_extension])
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="created_at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="updated_at")

    @staticmethod
    def random(count):
        total_count = Article.objects.count()
        if total_count == 0:
            raise Article.DoesNotExist

        if count >= total_count:
            return Article.objects.all()

        random_indices = random.sample(range(total_count), count)
        random_articles = Article.objects.filter(pk__in=random_indices)
        return random_articles
