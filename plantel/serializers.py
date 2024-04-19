from rest_framework import serializers
from universidad.serializers import UniversidadSerializer
from users.serializers import UserSerializer
from .models import Plantel

class PlantelSerializer(serializers.ModelSerializer):
    """
    Un ModelSerializer automaticamente toma las validaciones de los campos de su modelo
    NotNull no es necesario, MinLength si.
    """
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    universidad = UniversidadSerializer(read_only=True)

    class Meta:
        model = Plantel
        # fields = "__all__"
        fields = (
            "id",
            "name",
            "codigo",
            "rfc",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "universidad",
        )

    @staticmethod
    def get_examples():
        return {
            "rfc": "RFC de la empresa",
            "codigo": "codigo de la institucion",
        }


class PlantelWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Plantel
        fields = (
            "name",
            "codigo",
            "rfc",
            "universidad",
        )

    @staticmethod
    def get_examples():
        return {
            "rfc": "RFC de la empresa",
            "codigo": "codigo de la institucion",
        }
