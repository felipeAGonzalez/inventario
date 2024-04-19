from django.db import models
from aula.models import Aula
from dispositivo.models import Dispositivo
from inventario.common.base import BaseModel

class AulaDispositivo(BaseModel):
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE, to_field='id')
    dispositivo = models.ForeignKey(Dispositivo, on_delete=models.CASCADE, to_field='id')
    history = models.BooleanField(default=False)

    class Meta:
        ordering = ["-id"]
        db_table = 'aula_dispositivo'

    def __str__(self):
        return f"{self.aula.codigo_aula} - {self.dispositivo.codigo_dispositivo}"