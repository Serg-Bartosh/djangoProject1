from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from socialnetwork.models import Article, CommentArticle, ArticleLike


class ArticlePageView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request, author, title):
        try:
            article = Article.objects.get(author=author, title=title)
        except Article.DoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)

        try:
            comments = CommentArticle.objects.filter(article=article)
        except CommentArticle.DoesNotExist:
            comments = []

        comments_count = comments.count()

        try:
            likes_count = ArticleLike.objects.filter(article=article, like=True).count()
            dislikes_count = ArticleLike.objects.filter(article=article, like=False).count()
        except ArticleLike.DoesNotExist:
            likes_count = 0
            dislikes_count = 0
        context = {'article': article,
                   'comments': comments,
                   'comments_count': comments_count,
                   'author': author,
                   'likes': likes_count,
                   'dislikes': dislikes_count}

        return render(request, 'templates/artecle/article.html',
                      context=context)
