from .models import Material
from .serializers import MaterialSerializer, MaterialWriteSerializer
from inventario.utils import generate_search_field
from inventario.common.base import BaseViewSet
from rest_framework.permissions import IsAuthenticated
from .filter import MaterialFilter


class MaterialViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated]
    default_serializer_class = MaterialSerializer
    filterset_class = MaterialFilter
    default_serializer_class = MaterialSerializer
    serializer_classes = {
        "list": MaterialSerializer,
        "retrieve": MaterialSerializer,
        "create": MaterialWriteSerializer,
        "update": MaterialWriteSerializer,
        "partial_update": MaterialWriteSerializer,
    }
    response_classes = {
        "create": MaterialSerializer,
        "update": MaterialSerializer,
        "partial_update": MaterialSerializer,
    }
    swagger_tags = ["api/material"]

    def get_queryset(self):
        return Material.objects.all()

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user, updated_by=self.request.user, search=generate_search_field(serializer.validated_data["name"]))
    
    def perform_update(self, serializer):
        if "name" in serializer.validated_data:
            serializer.validated_data["search"] = generate_search_field(serializer.validated_data["name"])
        return serializer.save(updated_by=self.request.user)