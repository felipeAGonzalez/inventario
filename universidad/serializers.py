from rest_framework import serializers
from django.core import validators
from .models import Universidad
from users.serializers import UserSerializer


class UniversidadSerializer(serializers.ModelSerializer):
    """
    Un ModelSerializer automaticamente toma las validaciones de los campos de su modelo
    NotNull no es necesario, MinLength si.
    """
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)

    class Meta:
        model = Universidad
        # fields = "__all__"
        fields = (
            "id",
            "name",
            "rfc",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        )

    @staticmethod
    def get_examples():
        return {
            "rfc": "RFC de la empresa",
        }


class UniversidadWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Universidad
        fields = (
            "name",
            "rfc",
        )

    @staticmethod
    def get_examples():
        return {
            "rfc": "RFC de la empresa",
        }
