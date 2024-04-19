from .models import Universidad
from .serializers import UniversidadSerializer, UniversidadWriteSerializer
from inventario.utils import generate_search_field
from inventario.common.base import BaseViewSet
from rest_framework.permissions import IsAuthenticated
from .filter import UniversidadFilter


class UniversidadViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated]
    default_serializer_class = UniversidadSerializer
    filterset_class = UniversidadFilter
    default_serializer_class = UniversidadSerializer
    serializer_classes = {
        "list": UniversidadSerializer,
        "retrieve": UniversidadSerializer,
        "create": UniversidadWriteSerializer,
        "update": UniversidadWriteSerializer,
        "partial_update": UniversidadWriteSerializer,
    }
    response_classes = {
        "create": UniversidadSerializer,
        "update": UniversidadSerializer,
        "partial_update": UniversidadSerializer,
    }
    swagger_tags = ["api/universidad"]

    def get_queryset(self):
        return Universidad.objects.all()

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user, updated_by=self.request.user, search=generate_search_field(serializer.validated_data["name"]))
    
    def perform_update(self, serializer):
        if "name" in serializer.validated_data:
            serializer.validated_data["search"] = generate_search_field(serializer.validated_data["name"])
        return serializer.save(updated_by=self.request.user)
