from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class LogoutView(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def get(request):
        logout(request)
        return HttpResponseRedirect(redirect_to='/main/')
