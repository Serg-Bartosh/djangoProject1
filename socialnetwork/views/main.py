from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from socialnetwork.models import Article, ArticleLike, CommentArticle


class MainView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):
        user = request.user
        context = {}
        try:
            articles = Article.random(10)
            article_data = []
            for article in articles:
                likes_count = ArticleLike.objects.filter(article=article, like=True).count()
                dislikes_count = ArticleLike.objects.filter(article=article, like=False).count()
                comments_count = CommentArticle.objects.filter(article=article).count()
                author = article.author
                article_data.append({
                    'article': article,
                    'likes_count': likes_count,
                    'dislikes_count': dislikes_count,
                    'author': author,
                    'comments': comments_count
                })
            context.update({'articles_with_likes': article_data})
        except Article.DoesNotExist:
            # TODO: fix
            c = 1
        context.update({'user': user})
        return render(request, 'templates/main/main.html', context=context)

    @staticmethod
    def post(request):
        return Response({'message': 'Only GET requests'})
