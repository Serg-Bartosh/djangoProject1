from rest_framework import serializers
from socialnetwork.models.photo import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['image']
