from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Pet
from .serializers import PetSerializer


class PetViewSet(ModelViewSet):
    serializer_class = PetSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            return Pet.objects.all()

        return Pet.objects.filter(owner=user)

    def perform_create(self, serializer):
        user = self.request.user

        if user.is_staff or user.is_superuser:
            serializer.save()
        else:
            serializer.save(owner=user)

