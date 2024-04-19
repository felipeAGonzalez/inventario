from django.db import models
from inventario.common.base import BaseModel
from universidad.models import Universidad

class Plantel(BaseModel):
    name = models.CharField(max_length=255, help_text="Nombre de la universidad")
    search = models.CharField(max_length=255, help_text="Búsqueda asociada para la universidad")
    codigo = models.CharField(blank=True, default="", max_length=255, help_text="Razón social de la universidad")
    rfc = models.CharField(max_length=13, help_text="Registro Federal de Contribuyentes de la universidad")
    universidad = models.ForeignKey(Universidad, related_name='universidad_link', on_delete=models.CASCADE, to_field='id', help_text="Corporativo al que pertenece la empresa")

    class Meta:
        ordering = ["-id"]
        db_table = 'plantel'

    def __str__(self):
        return self.name