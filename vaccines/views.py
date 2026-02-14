from rest_framework.viewsets import ModelViewSet
from .models import Vaccine
from .serializers import VaccineSerializer
from .permissions import IsAdminOrReadOnly


class VaccineViewSet(ModelViewSet):
    queryset = Vaccine.objects.all()
    serializer_class = VaccineSerializer
    permission_classes = [IsAdminOrReadOnly]
