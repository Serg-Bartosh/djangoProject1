from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from socialnetwork.permissions.is_owner import IsOwnerOrReadOnly
from socialnetwork.serializers.article.article import ArticleSerializer


class ArticleView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    # TODO: edit article
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)
