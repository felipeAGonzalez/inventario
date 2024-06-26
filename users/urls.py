from .views import UserViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"users", UserViewSet, basename="users")
urlpatterns = router.urls