from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from users.models import Users
from rest_framework.test import APITestCase
from universidad.models import Universidad
from plantel.models import Plantel
from material.models import Material
from dispositivo.models import Dispositivo
from aula.models import Aula
from universidad.serializers import UniversidadSerializer
from .models import Edificio
from plantel.serializers import PlantelSerializer
from .serializers import EdificioSerializer
from rest_framework_simplejwt.tokens import AccessToken

class PlantelTests(APITestCase):
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

    def test_create_edificio(self):
        url = reverse('edificio-list')
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
            'plantel': plantel.id,
            'name': 'test Plantel',
            'ubicacion': '123 Main St',
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(url, edificio_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_edificio(self):
        url = reverse('edificio-list')
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
        Edificio.objects.create(**edificio_data)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_edificio(self):
        url = reverse('edificio-list')
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
        url =  reverse('edificio-detail', kwargs={'pk': edificio.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_edificio(self):
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
        url =  reverse('edificio-detail', kwargs={'pk': edificio.pk})
        edificio_data = {
            'plantel': plantel.pk,
            'name': 'Pretyre',
            'ubicacion': '123 Main St',
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.put(url, edificio_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        edificio.refresh_from_db()
        self.assertEqual(edificio.name, edificio_data['name'])

    def test_partial_update_edificio(self):
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
        url =  reverse('edificio-detail', kwargs={'pk': edificio.pk})
        partial_data = {'ubicacion': '456 Elm St'}
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.patch(url, partial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        edificio.refresh_from_db()
        self.assertEqual(edificio.ubicacion, partial_data['ubicacion'])


    def test_delete_edificio(self):
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
        url =  reverse('edificio-detail', kwargs={'pk': edificio.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Edificio.objects.count(), 0)
