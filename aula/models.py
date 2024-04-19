from django.db import models
from edificio.models import Edificio
from inventario.common.base import BaseModel

class Aula(BaseModel):
    edificio = models.ForeignKey(Edificio, on_delete=models.CASCADE, to_field='id')
    codigo_aula = models.CharField(max_length=255)   
    search = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]
        db_table = 'aula'

    def __str__(self):
        return self.codigo_aula