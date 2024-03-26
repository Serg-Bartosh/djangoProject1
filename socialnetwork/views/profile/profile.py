from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
from rest_framework.views import APIView

from socialnetwork.models import Avatar, Article, User, ArticleLike
from socialnetwork.permissions.is_owner import IsOwnerOrReadOnly
from socialnetwork.serializers.profile.avatar import AvatarSerializer
from socialnetwork.models import CommentArticle, Photo


class ProfileView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    @staticmethod
    def get(request, username):
        user = User.objects.get(username=username)
        try:
            avatar = Avatar.objects.get(user_id=user)
        except Avatar.DoesNotExist:
            avatar = None
        photo = Photo.objects.filter(user=user)
        articles = Article.objects.filter(author=user)
        articles_info = []
        for article in articles:
            like = ArticleLike.objects.filter(article=article, like=True).count()
            dislike = ArticleLike.objects.filter(article=article, like=False).count()
            comments_count = CommentArticle.objects.filter(article=article).count()
            articles_info.append({
                'image': article.image.url,
                'title': article.title,
                'context': article.content,
                'likes': like,
                'dislikes': dislike,
                'comments_count': comments_count,
                'created_at': article.created_at,
                'updated_at': article.updated_at,
                'author': article.author_id,
            })

        context = {'user': user, 'avatar': avatar, 'photos': photo, 'articles_info': articles_info}
        return render(request, 'templates/profile/profile.html', context=context)

    @staticmethod
    def update_avatar(avatar, image_data):
        avatar.image.delete()
        avatar.image = image_data
        avatar.save()

    # TODO: edit profile
    @staticmethod
    def post(request, username):
        user = User.objects.get(username=username)
        serializer = AvatarSerializer(data=request.data)
        if serializer.is_valid():
            try:
                existing_avatar = Avatar.objects.get(user=user)
            except Avatar.DoesNotExist:
                serializer.save(user=user)
                return Response(status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)
