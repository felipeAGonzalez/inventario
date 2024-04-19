from .models import AulaDispositivo
from .serializers import AulaDispositivoSerializer, AulaDispositivoWriteSerializer
from inventario.common.base import BaseViewSet
from rest_framework.permissions import IsAuthenticated
from .filter import AulaDispositivoFilter


class AulaDispositivoViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated]
    default_serializer_class = AulaDispositivoSerializer
    filterset_class = AulaDispositivoFilter
    default_serializer_class = AulaDispositivoSerializer
    serializer_classes = {
        "list": AulaDispositivoSerializer,
        "retrieve": AulaDispositivoSerializer,
        "create": AulaDispositivoWriteSerializer,
        "update": AulaDispositivoWriteSerializer,
        "partial_update": AulaDispositivoWriteSerializer,
    }
    response_classes = {
        "create": AulaDispositivoSerializer,
        "update": AulaDispositivoSerializer,
        "partial_update": AulaDispositivoSerializer,
    }
    swagger_tags = ["api/aula_dispositivo"]

    def get_queryset(self):
        return AulaDispositivo.objects.all()

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user, updated_by=self.request.user)
    
    def perform_update(self, serializer):
        return serializer.save(updated_by=self.request.user)