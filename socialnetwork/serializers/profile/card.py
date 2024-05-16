from rest_framework import serializers

from socialnetwork.models import User


class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['card_number', 'card_expiry_date', 'card_holder_name']
