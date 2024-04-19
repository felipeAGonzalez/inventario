from .views import UniversidadViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"universidad", UniversidadViewSet, basename="universidad")
urlpatterns = router.urls
