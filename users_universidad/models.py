from django.db import models
from universidad.models import Universidad
from inventario.common.base import BaseModel
from django.contrib.auth import get_user_model

class UsersUniversidad(BaseModel):
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE, to_field='id')
    user = models.ForeignKey(
        get_user_model(),
        default=None,
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        ordering = ["-id"]
        db_table = 'users_universidad'

    def __str__(self):
        return f"{self.universidad.name} - {self.user.get_username()}"