from .views import DispositivoViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"dispositivo", DispositivoViewSet, basename="dispositivo")
urlpatterns = router.urls
