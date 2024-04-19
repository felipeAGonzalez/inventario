from rest_framework import serializers
from users.serializers import UserSerializer
from .models import Material


class MaterialSerializer(serializers.ModelSerializer):
    """
    Un ModelSerializer automaticamente toma las validaciones de los campos de su modelo
    NotNull no es necesario, MinLength si.
    """
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)

    class Meta:
        model = Material
        # fields = "__all__"
        fields = (
            "id",
            "name",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
        )



class MaterialWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Material
        fields = (
            "name",
        )
