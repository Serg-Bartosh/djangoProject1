from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get(request):
        user = request.user
        context = {}
        if user.is_authenticated:
            context.update({'user': user})
        return render(request, 'templates/profile/profile.html', context=context)

    # TODO: edit profile
    # @staticmethod
    # def post(request):
