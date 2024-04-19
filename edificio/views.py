from .models import Edificio
from .serializers import EdificioSerializer, EdificioWriteSerializer
from inventario.utils import generate_search_field
from inventario.common.base import BaseViewSet
from rest_framework.permissions import IsAuthenticated
from .filter import EdificioFilter


class EdificioViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated]
    default_serializer_class = EdificioSerializer
    filterset_class = EdificioFilter
    default_serializer_class = EdificioSerializer
    serializer_classes = {
        "list": EdificioSerializer,
        "retrieve": EdificioSerializer,
        "create": EdificioWriteSerializer,
        "update": EdificioWriteSerializer,
        "partial_update": EdificioWriteSerializer,
    }
    response_classes = {
        "create": EdificioSerializer,
        "update": EdificioSerializer,
        "partial_update": EdificioSerializer,
    }
    swagger_tags = ["api/edificio"]

    def get_queryset(self):
        return Edificio.objects.all()

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user, updated_by=self.request.user, search=generate_search_field(serializer.validated_data["name"]))
    
    def perform_update(self, serializer):
        if "name" in serializer.validated_data:
            serializer.validated_data["search"] = generate_search_field(serializer.validated_data["name"])
        return serializer.save(updated_by=self.request.user)