from rest_framework import serializers
from .models import Vaccine


class VaccineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccine
        fields = ["id", "name", "manufacturer", "species_target", "doses_required", "days_between_doses"]
