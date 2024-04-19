from .views import MaterialViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"material", MaterialViewSet, basename="material")
urlpatterns = router.urls
