from rest_framework import serializers
from edificio.serializers import EdificioSerializer
from users.serializers import UserSerializer
from .models import Aula


class AulaSerializer(serializers.ModelSerializer):
    """
    Un ModelSerializer automaticamente toma las validaciones de los campos de su modelo
    NotNull no es necesario, MinLength si.
    """
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    edificio = EdificioSerializer(read_only=True)

    class Meta:
        model = Aula
        # fields = "__all__"
        fields = (
            "id",
            "edificio",
            "codigo_aula",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        )



class AulaWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Aula
        fields = (
            "codigo_aula",
            "edificio",
        )
