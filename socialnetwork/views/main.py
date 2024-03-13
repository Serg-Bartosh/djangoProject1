from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class MainView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):
        user = request.user
        context = {}
        if user.is_authenticated:
            context.update({'user': user})
        return render(request, 'templates/main/main.html', context=context)

    @staticmethod
    def post(request):
        return Response({'message': 'Only GET requests'})
