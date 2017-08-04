import time
from rest_framework import serializers
from .models import Player

class PlayerSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Player
        fields = ('timestamp', 'player_type', 'player_id')
