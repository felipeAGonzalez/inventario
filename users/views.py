from .serializers import UserSerializer
from .models import Users

from inventario.common.base import BaseViewSet
from .filter import UserFilter
from inventario.permissions import UserPermission


class UserViewSet(BaseViewSet):
    permission_classes = [UserPermission]
    default_serializer_class = UserSerializer
    filterset_class = UserFilter
    default_serializer_class = UserSerializer
    serializer_classes = {
        "list": UserSerializer,
        "retrieve": UserSerializer,
        "create": UserSerializer,
        "update": UserSerializer,
        "partial_update": UserSerializer,
    }
    response_classes = {
        "create": UserSerializer,
        "update": UserSerializer,
        "partial_update": UserSerializer,
    }
    swagger_tags = ["api/user"]

    def get_queryset(self):
        return Users.objects.order_by('-id').filter(deleted=False)