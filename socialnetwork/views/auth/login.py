from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from socialnetwork.serializers.auth.login import LoginSerializer


class LoginView(APIView):
    permission_classes = [~IsAuthenticated]

    @staticmethod
    def get(request):
        return render(request, 'templates/profile/login.html')

    @staticmethod
    def post(request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(request, email=serializer.validated_data['email'],
                                password=serializer.validated_data['password'])
            if user is not None:
                login(request, user)
                username = user.username
                return HttpResponseRedirect(reverse('profile', kwargs={'username': username}))
        return Response(status=HTTP_400_BAD_REQUEST)
