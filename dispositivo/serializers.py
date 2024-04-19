from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Dispositivo


class DispositivoSerializer(serializers.ModelSerializer):
    """
    Un ModelSerializer automaticamente toma las validaciones de los campos de su modelo
    NotNull no es necesario, MinLength si.
    """
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)

    class Meta:
        model = Dispositivo
        # fields = "__all__"
        fields = (
            "id",
            "codigo_dispositivo",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        )



class DispositivoWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dispositivo
        fields = (
            "codigo_dispositivo",
        )