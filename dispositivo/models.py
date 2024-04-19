from django.db import models
from inventario.common.base import BaseModel

class Dispositivo(BaseModel):
    codigo_dispositivo = models.CharField(max_length=255)    
    search = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]
        db_table = 'dispositivo'

    def __str__(self):
        return self.codigo_dispositivo