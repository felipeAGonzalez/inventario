from rest_framework import serializers
from users.serializers import UserSerializer
from dispositivo.serializers import DispositivoSerializer
from material.serializers import MaterialSerializer
from .models import DispositivoMaterial


class DispositivoMaterialSerializer(serializers.ModelSerializer):
    """
    Un ModelSerializer automaticamente toma las validaciones de los campos de su modelo
    NotNull no es necesario, MinLength si.
    """
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    dispositivo = DispositivoSerializer(read_only=True)
    material = MaterialSerializer(read_only=True)

    class Meta:
        model = DispositivoMaterial
        fields = (
            "id",
            "dispositivo",
            "material",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        )



class DispositivoMaterialWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = DispositivoMaterial
        fields = (
            "dispositivo",
            "material",
            "history"
        )
