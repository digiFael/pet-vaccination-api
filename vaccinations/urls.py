from rest_framework.routers import DefaultRouter
from .views import VaccinationRecordViewSet

router = DefaultRouter()
router.register("vaccinations", VaccinationRecordViewSet, basename="vaccinations")

urlpatterns = router.urls