from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from users.models import Users
from rest_framework.test import APITestCase
from universidad.models import Universidad
from edificio.models import Edificio
from universidad.serializers import UniversidadSerializer
from .models import Plantel
from .serializers import PlantelSerializer
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

    def test_create_plantel(self):
        url = reverse('plantel-list')
        universidad_data = {
            'name': 'Setenal',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        universidad=Universidad.objects.create(**universidad_data)
        plantel_data = {
            'universidad': universidad.id,
            'name': 'test Plantel',
            'codigo': '123 Main St',
            'rfc': '555-1234'
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(url, plantel_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_plantel(self):
        url = reverse('plantel-list')
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
        Plantel.objects.create(**plantel_data)
        plantel_data = {
            'universidad': universidad,
            'name': 'Guadalajara',
            'codigo': '123 Main St',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        Plantel.objects.create(**plantel_data)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_retrieve_plantel(self):
        url = reverse('plantel-list')
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
        url =  reverse('plantel-detail', kwargs={'pk': plantel.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_plantel(self):
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
        url =  reverse('plantel-detail', kwargs={'pk': plantel.pk})
        comapny_data = {
            'universidad': universidad.pk,
            'name': 'Pretyre',
            'codigo': '698 Main St',
            'rfc': '444-1234'
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.put(url, comapny_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        plantel.refresh_from_db()
        self.assertEqual(plantel.name, comapny_data['name'])

    def test_partial_update_plantel(self):
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
        url =  reverse('plantel-detail', kwargs={'pk': plantel.pk})
        partial_data = {'codigo': '456 Elm St'}
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.patch(url, partial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        plantel.refresh_from_db()
        self.assertEqual(plantel.codigo, partial_data['codigo'])


    def test_delete_plantel(self):
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
        url =  reverse('plantel-detail', kwargs={'pk': plantel.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Plantel.objects.count(), 0)
