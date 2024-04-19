from .views import DispositivoMaterialViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"dispositivo_material", DispositivoMaterialViewSet, basename="dispositivo_material")
urlpatterns = router.urls
