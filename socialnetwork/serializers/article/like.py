from rest_framework import serializers
from socialnetwork.models.like import ArticleLike


class LikeArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleLike
        fields = ['like']
