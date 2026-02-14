from rest_framework import serializers
from .models import VaccinationRecord


class VaccinationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = VaccinationRecord
        fields = ["id", "pet", "vaccine", "applied_at", "dose_number", "notes", "applied_by"]
        read_only_fields = ["applied_by"]