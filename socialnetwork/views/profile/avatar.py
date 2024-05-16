from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from socialnetwork.models import Avatar, User
from socialnetwork.permissions.is_owner import IsOwnerOrReadOnly
from socialnetwork.serializers.profile.avatar import AvatarSerializer


class AvatarView(APIView):
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    @staticmethod
    def update_avatar(avatar, image_data):
        avatar.image.delete()
        avatar.image = image_data
        avatar.save()

    # TODO: edit auth
    def post(self, request, username):
        user = User.objects.get(username=username)
        serializer = AvatarSerializer(data=request.data)
        if serializer.is_valid():
            try:
                existing_avatar = Avatar.objects.get(user=user)
            except Avatar.DoesNotExist:
                serializer.save(user=user)
                return Response(status=HTTP_200_OK)
            AvatarView.update_avatar(existing_avatar, serializer.validated_data['image'])
            return Response(status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)
