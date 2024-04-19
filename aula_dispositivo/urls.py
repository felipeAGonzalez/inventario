from .views import AulaDispositivoViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"aula_dispositivo", AulaDispositivoViewSet, basename="aula_dispositivo")
urlpatterns = router.urls
