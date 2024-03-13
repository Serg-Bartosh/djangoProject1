from django.contrib.auth.models import BaseUserManager

from socialnetwork.models import User


class UserManager(BaseUserManager):
    @staticmethod
    def create(validated_data):
        if not validated_data['user_name']:
            raise ValueError('Users must have an username')
        if not validated_data['email']:
            raise ValueError('Users must have an email address')
        if not validated_data['password']:
            raise ValueError('Users must have an password')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()
