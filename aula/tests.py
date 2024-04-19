from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from users.models import Users
from rest_framework.test import APITestCase
from universidad.models import Universidad
from plantel.models import Plantel
from universidad.serializers import UniversidadSerializer
from .models import Aula
from edificio.models import Edificio
from edificio.serializers import EdificioSerializer
from .serializers import AulaSerializer
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

    def test_create_aula(self):
        url = reverse('aula-list')
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
            'edificio': edificio.id,
            'codigo_aula': 'XX15',
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(url,aula_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_aula(self):
        url = reverse('aula-list')
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
        Aula.objects.create(**aula_data)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_aula(self):
        url = reverse('aula-list')
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
        url =  reverse('aula-detail', kwargs={'pk': aula.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_aula(self):
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
        url =  reverse('aula-detail', kwargs={'pk': aula.pk})
        aula_data = {
            'edificio': edificio.id,
            'codigo_aula': 'ZZ15',
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.put(url, aula_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        aula.refresh_from_db()
        self.assertEqual(aula.codigo_aula, aula_data['codigo_aula'])


    def test_delete_aula(self):
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
        url =  reverse('aula-detail', kwargs={'pk': aula.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Aula.objects.count(), 0)
    