# Generated by Django 4.2 on 2024-04-13 01:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('plantel', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Edificio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(help_text='Nombre de la universidad', max_length=255)),
                ('search', models.CharField(help_text='Búsqueda asociada para la universidad', max_length=255)),
                ('ubicacion', models.CharField(help_text='Dirección de la edificio', max_length=255)),
                ('created_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('plantel', models.ForeignKey(help_text='Empresa a la que pertenece la edificio', on_delete=django.db.models.deletion.CASCADE, related_name='plantel_link', to='plantel.plantel')),
                ('updated_by', models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_updated', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'edificio',
                'ordering': ['-id'],
            },
        ),
    ]
