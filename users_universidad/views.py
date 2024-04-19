from .models import UsersUniversidad
from .serializers import UsersUniversidadSerializer, UsersUniversidadWriteSerializer
from inventario.common.base import BaseViewSet
from rest_framework.permissions import IsAuthenticated
from .filter import UsersUniversidadFilter


class UsersUniversidadViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated]
    default_serializer_class = UsersUniversidadSerializer
    filterset_class = UsersUniversidadFilter
    default_serializer_class = UsersUniversidadSerializer
    serializer_classes = {
        "list": UsersUniversidadSerializer,
        "retrieve": UsersUniversidadSerializer,
        "create": UsersUniversidadWriteSerializer,
        "update": UsersUniversidadWriteSerializer,
        "partial_update": UsersUniversidadWriteSerializer,
    }
    response_classes = {
        "create": UsersUniversidadSerializer,
        "update": UsersUniversidadSerializer,
        "partial_update": UsersUniversidadSerializer,
    }
    swagger_tags = ["api/users_universidad"]

    def get_queryset(self):
        return UsersUniversidad.objects.all()

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user, updated_by=self.request.user)
    
    def perform_update(self, serializer):
        return serializer.save(updated_by=self.request.user)