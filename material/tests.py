from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from users.models import Users
from rest_framework.test import APITestCase
from universidad.models import Universidad
from plantel.models import Plantel
from universidad.serializers import UniversidadSerializer
from .models import Material
from .serializers import MaterialSerializer
from rest_framework_simplejwt.tokens import AccessToken
from decimal import Decimal

class MaterialTests(APITestCase):
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

    def test_create_material(self):
        url = reverse('material-list')
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
       
        material_data = {
            'name': 'Juan',
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(url,material_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_material(self):
        url = reverse('material-list')
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
       
        material_data = {
            'name': 'Juan',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        Material.objects.create(**material_data)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_material(self):
        url = reverse('material-list')
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
       
        material_data = {
            'name': 'Juan',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        material=Material.objects.create(**material_data)
        url =  reverse('material-detail', kwargs={'pk': material.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_material(self):
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
       
        material_data = {
            'name': 'Juan',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        material=Material.objects.create(**material_data)
        url =  reverse('material-detail', kwargs={'pk': material.pk})
        material_data = {
            'name': 'Juan R',
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.put(url, material_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        material.refresh_from_db()
        self.assertEqual(material.name, material_data['name'])

    def test_delete_material(self):
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
       
        material_data = {
            'name': 'Juan',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        material=Material.objects.create(**material_data)
        url =  reverse('material-detail', kwargs={'pk': material.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Material.objects.count(), 0)
    