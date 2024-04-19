from .models import Aula
from .serializers import AulaSerializer, AulaWriteSerializer
from inventario.utils import generate_search_field
from inventario.common.base import BaseViewSet
from rest_framework.permissions import IsAuthenticated
from .filter import AulaFilter

from material.models import Material
from dispositivo.models import Dispositivo
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework import status
from edificio.models import Edificio
from aula_dispositivo.models import AulaDispositivo
from aula_dispositivo.serializers import AulaDispositivoWriteSerializer
from rest_framework.parsers import FileUploadParser
from django.http import HttpResponse
import io
from django.db import transaction




class AulaViewSet(BaseViewSet):
    permission_classes = [IsAuthenticated]
    default_serializer_class = AulaSerializer
    filterset_class = AulaFilter
    default_serializer_class = AulaSerializer
    serializer_classes = {
        "list": AulaSerializer,
        "retrieve": AulaSerializer,
        "create": AulaWriteSerializer,
        "update": AulaWriteSerializer,
        "partial_update": AulaWriteSerializer,
    }
    response_classes = {
        "create": AulaSerializer,
        "update": AulaSerializer,
        "partial_update": AulaSerializer,
    }
    swagger_tags = ["api/aula"]

    def get_queryset(self):
        return Aula.objects.all()

    def perform_create(self, serializer):
        return serializer.save(created_by=self.request.user, updated_by=self.request.user, search=generate_search_field(serializer.validated_data["codigo_aula"]))
    
    def perform_update(self, serializer):
        if "codigo_aula" in serializer.validated_data:
            serializer.validated_data["search"] = generate_search_field(serializer.validated_data["codigo_aula"])
        return serializer.save(updated_by=self.request.user)
    