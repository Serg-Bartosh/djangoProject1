from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from socialnetwork.serializers.registration import RegistrationSerializer
from socialnetwork.models import User
from django.contrib.auth import login, authenticate


class RegistrationView(APIView):
    permission_classes = [~IsAuthenticated]

    @staticmethod
    def get(request):
        return render(request, 'templates/profile/registration.html', status=HTTP_200_OK)

    @staticmethod
    def post(request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            hashed_password = make_password(serializer.validated_data['password'])
            user = User.objects.create(
                email=serializer.validated_data['email'],
                username=serializer.validated_data['username'],
                password=hashed_password,
                first_name=serializer.validated_data.get('first_name', ''),
                last_name=serializer.validated_data.get('last_name', ''),
            )
            login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            authenticate(username=serializer.validated_data['username'],
                         password=serializer.validated_data['password'])
            return HttpResponseRedirect(redirect_to='/main/profile')
        return Response(status=HTTP_400_BAD_REQUEST)
