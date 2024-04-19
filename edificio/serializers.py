from rest_framework import serializers
from plantel.serializers import PlantelSerializer
from users.serializers import UserSerializer
from .models import Edificio

class EdificioSerializer(serializers.ModelSerializer):
    """
    Un ModelSerializer automaticamente toma las validaciones de los campos de su modelo
    NotNull no es necesario, MinLength si.
    """
    created_by = UserSerializer(read_only=True)
    updated_by = UserSerializer(read_only=True)
    plantel = PlantelSerializer(read_only=True)

    class Meta:
        model = Edificio
        # fields = "__all__"
        fields = (
            "id",
            "name",
            "ubicacion",
            "created_at",
            "updated_at",
            "created_by",
            "updated_by",
            "plantel",
        )



class EdificioWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Edificio
        fields = (
            "name",
            "ubicacion",
            "plantel",
        )
