from .views import UsersUniversidadViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r"users_universidad", UsersUniversidadViewSet, basename="users_universidad")
urlpatterns = router.urls
