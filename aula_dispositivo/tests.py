from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from users.models import Users
from rest_framework.test import APITestCase
from universidad.models import Universidad
from plantel.models import Plantel
from aula.models import Aula
from dispositivo.models import Dispositivo
from .models import AulaDispositivo
from edificio.models import Edificio
from rest_framework_simplejwt.tokens import AccessToken

class AulaTests(APITestCase):
    def setUp(self):
        self.user_root = {
            "name": "soporte",
            "last_name_1": "setenal",
            "email": "root@setenal.mx",
            "password": "jesco814",
            "preferred_language": "en",
        }
        self.user = Users.objects.create(**self.user_root)
        self.user.set_password('jesco814')
        self.user.save()
        self.access_token = AccessToken.for_user(self.user)

    def test_create_aula_dispositivo(self):
        url = reverse('aula_dispositivo-list')
        universidad_data = {
            'name': 'Setenal',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        universidad=Universidad.objects.create(**universidad_data)
        plantel_data = {
            'universidad': universidad,
            'name': 'Morelia',
            'codigo': '123 Main St',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        plantel=Plantel.objects.create(**plantel_data)
        edificio_data = {
            'plantel': plantel,
            'name': 'Guadalajara',
            'ubicacion': '123 Main St',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        edificio=Edificio.objects.create(**edificio_data)
        aula_data = {
            'edificio': edificio,
            'codigo_aula': 'XX15',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        aula=Aula.objects.create(**aula_data)
        dispositivo_data = {
            'codigo_dispositivo': '88RR',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        dispositivo = Dispositivo.objects.create(**dispositivo_data)
        aula_dispositivo_data = {
            'dispositivo': dispositivo.pk,
            'aula': aula.pk,
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(url,aula_dispositivo_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_aula_dispositivo(self):
        url = reverse('aula_dispositivo-list')
        universidad_data = {
            'name': 'Setenal',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        universidad=Universidad.objects.create(**universidad_data)
        plantel_data = {
            'universidad': universidad,
            'name': 'Morelia',
            'codigo': '123 Main St',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        plantel=Plantel.objects.create(**plantel_data)
        edificio_data = {
            'plantel': plantel,
            'name': 'Guadalajara',
            'ubicacion': '123 Main St',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        edificio=Edificio.objects.create(**edificio_data)
        aula_data = {
            'edificio': edificio,
            'codigo_aula': 'XX15',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        aula=Aula.objects.create(**aula_data)
        dispositivo_data = {
            'codigo_dispositivo': '88RR',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        dispositivo = Dispositivo.objects.create(**dispositivo_data)
        aula_dispositivo_data = {
            'dispositivo': dispositivo,
            'aula': aula,
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        AulaDispositivo.objects.create(**aula_dispositivo_data)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_aula_dispositivo(self):
        universidad_data = {
            'name': 'Setenal',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        universidad=Universidad.objects.create(**universidad_data)
        plantel_data = {
            'universidad': universidad,
            'name': 'Morelia',
            'codigo': '123 Main St',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        plantel=Plantel.objects.create(**plantel_data)
        edificio_data = {
            'plantel': plantel,
            'name': 'Guadalajara',
            'ubicacion': '123 Main St',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        edificio=Edificio.objects.create(**edificio_data)
        aula_data = {
            'edificio': edificio,
            'codigo_aula': 'XX15',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        aula=Aula.objects.create(**aula_data)
        dispositivo_data = {
            'codigo_dispositivo': '88RR',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        dispositivo = Dispositivo.objects.create(**dispositivo_data)
        aula_dispositivo_data = {
            'dispositivo': dispositivo,
            'aula': aula,
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        aula_dispositivo=AulaDispositivo.objects.create(**aula_dispositivo_data)
        url =  reverse('aula_dispositivo-detail', kwargs={'pk': aula_dispositivo.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_aula_dispositivo(self):
        universidad_data = {
            'name': 'Setenal',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        universidad=Universidad.objects.create(**universidad_data)
        plantel_data = {
            'universidad': universidad,
            'name': 'Morelia',
            'codigo': '123 Main St',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        plantel=Plantel.objects.create(**plantel_data)
        edificio_data = {
            'plantel': plantel,
            'name': 'Guadalajara',
            'ubicacion': '123 Main St',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        edificio=Edificio.objects.create(**edificio_data)
        aula_data = {
            'edificio': edificio,
            'codigo_aula': 'XX15',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        aula=Aula.objects.create(**aula_data)
        dispositivo_data = {
            'codigo_dispositivo': '88RR',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        dispositivo = Dispositivo.objects.create(**dispositivo_data)
        aula_dispositivo_data = {
            'dispositivo': dispositivo,
            'aula': aula,
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        aula_dispositivo=AulaDispositivo.objects.create(**aula_dispositivo_data)
        url =  reverse('aula_dispositivo-detail', kwargs={'pk': aula_dispositivo.pk})
        aula_data = {
            'dispositivo': dispositivo.id,
            'aula': aula.id,
            'history': True,
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.put(url, aula_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        aula_dispositivo.refresh_from_db()
        self.assertEqual(aula_dispositivo.history, aula_data['history'])

    def test_delete_aula_dispositivo(self):
        universidad_data = {
            'name': 'Setenal',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        universidad=Universidad.objects.create(**universidad_data)
        plantel_data = {
            'universidad': universidad,
            'name': 'Morelia',
            'codigo': '123 Main St',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        plantel=Plantel.objects.create(**plantel_data)
        edificio_data = {
            'plantel': plantel,
            'name': 'Guadalajara',
            'ubicacion': '123 Main St',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        edificio=Edificio.objects.create(**edificio_data)
        aula_data = {
            'edificio': edificio,
            'codigo_aula': 'XX15',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        aula=Aula.objects.create(**aula_data)
        dispositivo_data = {
            'codigo_dispositivo': '88RR',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        dispositivo = Dispositivo.objects.create(**dispositivo_data)
        aula_dispositivo_data = {
            'dispositivo': dispositivo,
            'aula': aula,
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        aula_dispositivo=AulaDispositivo.objects.create(**aula_dispositivo_data)
        url =  reverse('aula_dispositivo-detail', kwargs={'pk': aula_dispositivo.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(AulaDispositivo.objects.count(), 0)
    