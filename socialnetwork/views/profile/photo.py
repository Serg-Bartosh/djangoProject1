from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN
from rest_framework.views import APIView

from socialnetwork.permissions.is_owner import IsOwnerOrReadOnly
from socialnetwork.serializers.profile.photo import PhotoSerializer


class ProfilePhotoView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    # TODO: edit auth photo
    @staticmethod
    def post(request, username):
        serializer = PhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)
