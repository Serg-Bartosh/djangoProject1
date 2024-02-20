from rest_framework import serializers
from socialnetwork.model.abstract_user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'last_login', 'is_active',
                  'is_staff', 'is_superuser']
