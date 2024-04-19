from .models import DispositivoMaterial
from .serializers import DispositivoMaterialSerializer, DispositivoMaterialWriteSerializer
from inventario.common.base import BaseViewSet
from rest_framework.permissions import IsAuthenticated
from .filter import DispositivoMaterialFilter


class DispositivoMaterialViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated]
    default_serializer_class = DispositivoMaterialSerializer
    filterset_class = DispositivoMaterialFilter
    default_serializer_class = DispositivoMaterialSerializer
    serializer_classes = {
        "list": DispositivoMaterialSerializer,
        "retrieve": DispositivoMaterialSerializer,
        "create": DispositivoMaterialWriteSerializer,
        "update": DispositivoMaterialWriteSerializer,
        "partial_update": DispositivoMaterialWriteSerializer,
    }
    response_classes = {
        "create": DispositivoMaterialSerializer,
        "update": DispositivoMaterialSerializer,
        "partial_update": DispositivoMaterialSerializer,
    }
    swagger_tags = ["api/dispositivo_material"]

    def get_queryset(self):
        return DispositivoMaterial.objects.all()

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user, updated_by=self.request.user)
    
    def perform_update(self, serializer):
        return serializer.save(updated_by=self.request.user)