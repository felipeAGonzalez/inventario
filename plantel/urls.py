from .views import PlantelViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"plantel", PlantelViewSet, basename="plantel")
urlpatterns = router.urls
