from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Edificio
from edificio.models import Edificio
from aula.models import Aula

@receiver(pre_save, sender=Edificio)
def update_related_aula(sender, instance, **kwargs):
    if instance.pk: 
        try:
            previous_instance = Edificio.objects.get(pk=instance.pk)
            if previous_instance.deleted != instance.deleted:
                related_aulas = Aula.objects.filter(edificio=instance)
                for aula in related_aulas:
                    aula.deleted = instance.deleted
                    aula.save()
        except Aula.DoesNotExist:
            pass
