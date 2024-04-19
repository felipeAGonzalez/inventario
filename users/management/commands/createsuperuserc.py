from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from users.models import Users


class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **kwargs):
        user, created = Users.objects.get_or_create(
            email='root@root.com',
            defaults={
                'name': 'soporte',
                'last_name_1': 'setenal',
                'is_staff': True,
                'is_superuser': True,
            }
        )
        if created:
            user.set_password('jesco814')
            user.save()
            self.stdout.write(self.style.SUCCESS('Superuser created successfully!'))
        else:
            self.stdout.write(self.style.WARNING('Superuser already exists.'))
