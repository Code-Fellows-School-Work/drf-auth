from rest_framework import serializers
from .models import Doggo

class DoggoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doggo
        fields = (
            "id",
            "owner",
            "name",
            "description",
            "created_on"
        )