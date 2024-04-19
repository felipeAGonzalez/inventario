from rest_framework import serializers
from users.serializers import UserSerializer
from aula.serializers import AulaSerializer
from dispositivo.serializers import DispositivoSerializer
from .models import AulaDispositivo


class AulaDispositivoSerializer(serializers.ModelSerializer):
    """
    Un ModelSerializer automaticamente toma las validaciones de los campos de su modelo
    NotNull no es necesario, MinLength si.
    """
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    aula = AulaSerializer(read_only=True)
    dispositivo = DispositivoSerializer(read_only=True)

    class Meta:
        model = AulaDispositivo
        fields = (
            "id",
            "aula",
            "dispositivo",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        )



class AulaDispositivoWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = AulaDispositivo
        fields = (
            "aula",
            "dispositivo",
            "history"
        )
