from rest_framework import serializers
from socialnetwork.models.comment import CommentArticle


class CommentArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentArticle
        fields = ['comment']
