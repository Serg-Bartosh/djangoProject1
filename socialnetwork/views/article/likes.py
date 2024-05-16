from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from socialnetwork.models import Article
from socialnetwork.models.article.like import ArticleLike
from socialnetwork.serializers.article.like import LikeArticleSerializer
from socialnetwork.validator.article.like_validator import validate_like


class LikeArticleView(APIView):
    parser_classes = [FormParser, MultiPartParser]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, author, title):
        try:
            article = Article.objects.get(author=author, title=title)
        except Article.DoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)
        serializer = LikeArticleSerializer(data=request.POST)
        if serializer.is_valid():
            like_value = serializer.validated_data['like']
            print(like_value)
            try:
                user_like = ArticleLike.objects.get(user=request.user, article=article)

                if user_like.like == like_value:
                    return Response(status=HTTP_200_OK)
                user_like.like = like_value
                user_like.save()
                return Response(status=HTTP_200_OK)
            except ArticleLike.DoesNotExist:
                like = serializer.save(user=request.user, article=article, like=like_value)
                return Response(status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
