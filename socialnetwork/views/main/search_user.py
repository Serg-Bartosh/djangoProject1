from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated

from socialnetwork.models import Avatar
from socialnetwork.models.profile.user import User
from rest_framework.viewsets import ViewSet
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.response import Response
from socialnetwork.serializers.main.UserSetSerializer import UserSetSerializer


class SearchUserViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)

    def list(self, request, user_inf):
        print(user_inf)
        if not user_inf:
            return Response({'error': 'User info is required'}, status=HTTP_400_BAD_REQUEST)
        # TODO: проверить правильно ли работает
        queryset = User.objects.filter(
            username__icontains=user_inf
        ) | User.objects.filter(
            first_name__icontains=user_inf
        ) | User.objects.filter(
            last_name__icontains=user_inf
        )

        if not queryset:
            return Response({'error': 'User info is find'}, status=HTTP_400_BAD_REQUEST)

        serializer = UserSetSerializer(queryset, many=True)
        users = serializer.data

        for user in users:
            try:
                avatar = Avatar.objects.get(user_id=user['id'])
                user['avatar_url'] = avatar.image.url
            except Avatar.DoesNotExist:
                user['avatar_url'] = None

        print(users)
        return render(request, 'templates/main/search.html', {'users': users})
