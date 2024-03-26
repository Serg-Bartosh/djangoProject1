from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from socialnetwork.models import User


class SearchView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request, username):
        try:
            users = User.objects.filter(username__contains=username)
        except User.DoesNotExist:
            users = 'Doesn\'t exist'
        return render(request, template_name='templates/search.html', context={'users': users})
