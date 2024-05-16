from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from socialnetwork.models import Article
from socialnetwork.serializers.article.comment import CommentArticleSerializer


class CommentArticleView(APIView):
    parser_classes = [FormParser, MultiPartParser]
    permission_classes = [IsAuthenticated]

    @staticmethod
    def post(request, author, title):
        try:
            article = Article.objects.get(author=author, title=title)
        except Article.DoesNotExist:
            return Response(status=HTTP_400_BAD_REQUEST)

        serializer = CommentArticleSerializer(data=request.POST)
        if serializer.is_valid():
            comment = serializer.save(author=request.user, article=article)
            return Response(status=HTTP_200_OK)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
