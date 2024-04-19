from .views import AulaViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"aula", AulaViewSet, basename="aula")
urlpatterns = router.urls
