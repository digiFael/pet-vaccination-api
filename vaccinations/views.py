from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import VaccinationRecord
from .serializers import VaccinationRecordSerializer
from .permissions import IsStaffOrOwnerReadOnly


class VaccinationRecordViewSet(ModelViewSet):
    serializer_class = VaccinationRecordSerializer
    permission_classes = [IsAuthenticated, IsStaffOrOwnerReadOnly]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return VaccinationRecord.objects.select_related("pet", "vaccine").all()

        return VaccinationRecord.objects.select_related("pet", "vaccine").filter(pet__owner=user)

    def perform_create(self, serializer):
        serializer.save(applied_by=self.request.user)
