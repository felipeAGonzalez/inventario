from django.db import models
from inventario.common.base import BaseModel
from dispositivo.models import Dispositivo
from material.models import Material

class DispositivoMaterial(BaseModel):
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, to_field='id')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, to_field='id')
    history = models.BooleanField(default=False)

    class Meta:
        ordering = ["-id"]
        db_table = 'dispositivo_material'

    def __str__(self):
        return f"{self.dispositivo.codigo_aula} - {self.material.name}"

