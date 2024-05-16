from rest_framework import serializers
from socialnetwork.models.profile.user import User


class UserSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name']
