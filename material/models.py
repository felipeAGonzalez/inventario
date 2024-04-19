from django.db import models
from inventario.common.base import BaseModel

class Material(BaseModel):
    name = models.CharField(max_length=255)    
    search = models.CharField(max_length=255)

    class Meta:
        ordering = ["-id"]
        db_table = 'material'

    def __str__(self):
        return self.name