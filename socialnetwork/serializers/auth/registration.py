from rest_framework import serializers
from socialnetwork.models import User


# Django validators
# https://www.django-rest-framework.org/api-guide/validators/
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
