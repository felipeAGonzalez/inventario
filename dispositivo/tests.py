from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from users.models import Users
from rest_framework.test import APITestCase
from universidad.models import Universidad
from plantel.models import Plantel
from .models import Dispositivo
from .serializers import DispositivoSerializer
from rest_framework_simplejwt.tokens import AccessToken

class DispositivoTests(APITestCase):
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

    def test_create_dispositivo(self):
        url = reverse('dispositivo-list')
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
        dispositivo_data = {
            'codigo_dispositivo': '88RR',
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(url, dispositivo_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_dispositivo(self):
        url = reverse('dispositivo-list')
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
        dispositivo_data = {
            'codigo_dispositivo': '88RR',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        Dispositivo.objects.create(**dispositivo_data)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_dispositivo(self):
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

        dispositivo_data = {
            'codigo_dispositivo': '88RR',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        dispositivo=Dispositivo.objects.create(**dispositivo_data)
        url =  reverse('dispositivo-detail', kwargs={'pk': dispositivo.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_dispositivo(self):
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
        dispositivo_data = {
            'codigo_dispositivo': '88RR',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        dispositivo=Dispositivo.objects.create(**dispositivo_data)
        url =  reverse('dispositivo-detail', kwargs={'pk': dispositivo.pk})
        dispositivo_data = {
            'codigo_dispositivo': '99RR',
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.put(url, dispositivo_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dispositivo.refresh_from_db()
        self.assertEqual(dispositivo.codigo_dispositivo, dispositivo_data['codigo_dispositivo'])

    def test_delete_dispositivo(self):
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
        dispositivo_data = {
            'codigo_dispositivo': '88RR',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        dispositivo=Dispositivo.objects.create(**dispositivo_data)
        url =  reverse('dispositivo-detail', kwargs={'pk': dispositivo.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Dispositivo.objects.count(), 0)
