from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Plantel
from edificio.models import Edificio

@receiver(pre_save, sender=Plantel)
def update_related_subsidiaries(sender, instance, **kwargs):
    if instance.pk: 
        try:
            previous_instance = Plantel.objects.get(pk=instance.pk)
            if previous_instance.deleted != instance.deleted:
                related_subsidiaries = Edificio.objects.filter(plantel=instance)
                for edificio in related_subsidiaries:
                    edificio.deleted = instance.deleted
                    edificio.save()
        except Plantel.DoesNotExist:
            pass
