from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from socialnetwork.serializers import UserSerializer


class RegistrationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            pass
