from django.db import models
from inventario.common.base import BaseModel

class Universidad(BaseModel):
    name = models.CharField(max_length=255, help_text="Nombre de la universidad")
    search = models.CharField(max_length=255, help_text="Búsqueda asociada para la universidad")
    rfc = models.CharField(max_length=13, help_text="Registro Federal de Contribuyentes de la universidad")

    class Meta:
        ordering = ["-id"]
        db_table = 'universidad'

    def __str__(self):
        return self.name