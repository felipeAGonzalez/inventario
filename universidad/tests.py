from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from users.models import Users
from rest_framework.test import APITestCase
from .models import Universidad
from plantel.models import Plantel
from .serializers import UniversidadSerializer
from rest_framework_simplejwt.tokens import AccessToken

class UniversidadTests(APITestCase):
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

    def test_create_universidad(self):
        url = reverse('universidad-list')
        universidad_data = {
            'name': 'test Corp',
            'rfc': '555-1234'
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(url, universidad_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_universidad(self):
        url = reverse('universidad-list')
        universidad_data = {
            'name': 'Setenal',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        Universidad.objects.create(**universidad_data)
        universidad_data = {
            'name': 'SIAN',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        Universidad.objects.create(**universidad_data)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_universidad(self):
        universidad_data = {
            'name': 'Setenal',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        universidad=Universidad.objects.create(**universidad_data)
        url =  reverse('universidad-detail', kwargs={'pk': universidad.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_universidad(self):
        universidad_data = {
            'name': 'SIAN',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        universidad=Universidad.objects.create(**universidad_data)
        url =  reverse('universidad-detail', kwargs={'pk': universidad.pk})
        universidad_data = {
            'name': 'Pretyre',
            'rfc': '555-1234'
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.put(url, universidad_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        universidad.refresh_from_db()
        self.assertEqual(universidad.name, universidad_data['name'])


    def test_partial_update_universidad(self):
        universidad_data = {
            'name': 'Jesco',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        universidad=Universidad.objects.create(**universidad_data)
        url =  reverse('universidad-detail', kwargs={'pk': universidad.pk})
        partial_data = {'rfc': '456 Elm St'}
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.patch(url, partial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        universidad.refresh_from_db()
        self.assertEqual(universidad.rfc, partial_data['rfc'])


    def test_delete_universidad(self):
        universidad_data = {
            'name': 'CRM',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        universidad=Universidad.objects.create(**universidad_data)
        url =  reverse('universidad-detail', kwargs={'pk': universidad.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Universidad.objects.count(), 0)
