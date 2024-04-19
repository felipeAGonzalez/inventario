from inventario.common.base import BaseViewSet
from .models import Plantel
from .serializers import PlantelSerializer, PlantelWriteSerializer
from inventario.utils import generate_search_field
from rest_framework.permissions import IsAuthenticated
from .filter import PlantelFilter

class PlantelViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated]
    default_serializer_class = PlantelSerializer
    filterset_class = PlantelFilter
    default_serializer_class = PlantelSerializer
    serializer_classes = {
        "list": PlantelSerializer,
        "retrieve": PlantelSerializer,
        "create": PlantelWriteSerializer,
        "update": PlantelWriteSerializer,
        "partial_update": PlantelWriteSerializer,
    }
    response_classes = {
        "create": PlantelSerializer,
        "update": PlantelSerializer,
        "partial_update": PlantelSerializer,
    }
    swagger_tags = ["api/plantel"]

    def get_queryset(self):
        return Plantel.objects.all()

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user, updated_by=self.request.user, search=generate_search_field(serializer.validated_data["name"]))
    
    def perform_update(self, serializer):
        if "name" in serializer.validated_data:
            serializer.validated_data["search"] = generate_search_field(serializer.validated_data["name"])
        return serializer.save(updated_by=self.request.user)
