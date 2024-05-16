from rest_framework import serializers
from socialnetwork.models.article.like import ArticleLike


class LikeArticleSerializer(serializers.ModelSerializer):
    like = serializers.BooleanField(required=True)

    class Meta:
        model = ArticleLike
        fields = ['like']
