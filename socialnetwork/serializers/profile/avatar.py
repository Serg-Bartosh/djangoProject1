from rest_framework import serializers
from socialnetwork.models.profile.avatar import Avatar


class AvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avatar
        fields = ['image']
