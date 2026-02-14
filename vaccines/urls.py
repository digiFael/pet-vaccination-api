from rest_framework.routers import DefaultRouter
from .views import VaccineViewSet

router = DefaultRouter()
router.register("vaccines", VaccineViewSet, basename="vaccines")

urlpatterns = router.urls

