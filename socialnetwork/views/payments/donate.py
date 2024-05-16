from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from socialnetwork.models import Payment


class DonateView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def get(request):
        return render(request, 'templates/payment/donate.html')

    @staticmethod
    def post(request):
        return Response({'message': 'Only GET requests'})
