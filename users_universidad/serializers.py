from rest_framework import serializers
from universidad.serializers import UniversidadSerializer
from users.serializers import UserSerializer
from .models import UsersUniversidad


class UsersUniversidadSerializer(serializers.ModelSerializer):
    """
    Un ModelSerializer automaticamente toma las validaciones de los campos de su modelo
    NotNull no es necesario, MinLength si.
    """
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    universidad = UniversidadSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = UsersUniversidad
        fields = (
            "id",
            "universidad",
            "user",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        )



class UsersUniversidadWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = UsersUniversidad
        fields = (
            "universidad",
            "user",
        )
