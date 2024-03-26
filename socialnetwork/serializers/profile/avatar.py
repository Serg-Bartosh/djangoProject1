from rest_framework import serializers
from socialnetwork.models.avatar import Avatar


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ['image']
