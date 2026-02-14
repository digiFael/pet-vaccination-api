from rest_framework import serializers
from .models import Pet


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "name", "species", "breed", "birth_date", "owner"]
        read_only_fields = ["owner"]
