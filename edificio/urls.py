from .views import EdificioViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"edificio", EdificioViewSet, basename="edificio")
urlpatterns = router.urls
