from rest_framework import serializers
from socialnetwork.models.article.article import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['image', 'title', 'content']
