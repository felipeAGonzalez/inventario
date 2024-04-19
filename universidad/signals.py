from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Universidad
from plantel.models import Plantel

@receiver(pre_save, sender=Universidad)
def update_related_companies(sender, instance, **kwargs):
    if instance.pk: 
        try:
            previous_instance = Universidad.objects.get(pk=instance.pk)
            if previous_instance.deleted != instance.deleted:
                related_companies = Plantel.objects.filter(universidad=instance)
                for plantel in related_companies:
                    plantel.deleted = instance.deleted
                    plantel.save()
        except Universidad.DoesNotExist:
            pass
