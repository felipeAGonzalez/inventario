from django.db import models
from inventario.common.base import BaseModel
from plantel.models import Plantel

class Edificio(BaseModel):
    name = models.CharField(max_length=255, help_text="Nombre de la universidad")
    search = models.CharField(max_length=255, help_text="Búsqueda asociada para la universidad")
    ubicacion = models.CharField(max_length=255, help_text="Dirección de la edificio")  
    plantel = models.ForeignKey(Plantel, related_name='plantel_link', on_delete=models.CASCADE,  to_field='id', help_text="Empresa a la que pertenece la edificio") 

    class Meta:
        ordering = ["-id"]
        db_table = 'edificio'

    def __str__(self):
        return self.name