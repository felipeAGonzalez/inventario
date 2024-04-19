from django.urls import reverse
from rest_framework import status
from users.models import Users
from rest_framework.test import APITestCase
from universidad.models import Universidad
from .models import UsersUniversidad
from .serializers import UsersUniversidad
from rest_framework_simplejwt.tokens import AccessToken

class UsersUniversidadTests(APITestCase):
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

    def test_create_users_universidad(self):
        url = reverse('users_universidad-list')
        universidad_data = {
            'name': 'Setenal',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        universidad=Universidad.objects.create(**universidad_data)
        user_data = {
            "name": "Rafael",
            "last_name_1": "Hernandez",
            "last_name_2": "Espinosa",
            "email": "rafa@setenal.mx",
            "password": "jesco814",
            "preferred_language": "en"
        }
        user=Users.objects.create(**user_data)
        user_universidad_data = {
            'universidad': universidad.id,
            'user': user.id,
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.post(url, user_universidad_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_users_universidad(self):
        url = reverse('users_universidad-list')
        universidad_data = {
            'name': 'Setenal',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        universidad=Universidad.objects.create(**universidad_data)
        user_data = {
            "name": "Rafael",
            "last_name_1": "Hernandez",
            "last_name_2": "Espinosa",
            "email": "rafa@setenal.mx",
            "password": "jesco814",
            "preferred_language": "en"
        }
        user=Users.objects.create(**user_data)
        user_universidad_data = {
            'universidad': universidad,
            'user': user,
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        UsersUniversidad.objects.create(**user_universidad_data)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_users_universidad(self):
        url = reverse('users_universidad-list')
        universidad_data = {
            'name': 'Setenal',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        universidad=Universidad.objects.create(**universidad_data)
        user_data = {
            "name": "Rafael",
            "last_name_1": "Hernandez",
            "last_name_2": "Espinosa",
            "email": "rafa@setenal.mx",
            "password": "jesco814",
            "preferred_language": "en"
        }
        user=Users.objects.create(**user_data)
        user_universidad_data = {
            'universidad': universidad,
            'user': user,
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        user_universidad=UsersUniversidad.objects.create(**user_universidad_data)
        url =  reverse('users_universidad-detail', kwargs={'pk': user_universidad.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_users_universidad(self):
        universidad_data = {
            'name': 'Setenal',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        universidad=Universidad.objects.create(**universidad_data)
        user_data = {
            "name": "Rafael",
            "last_name_1": "Hernandez",
            "last_name_2": "Espinosa",
            "email": "rafa@setenal.mx",
            "password": "jesco814",
            "preferred_language": "en"
        }
        user=Users.objects.create(**user_data)
        user_universidad_data = {
            'universidad': universidad,
            'user': user,
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        user_universidad=UsersUniversidad.objects.create(**user_universidad_data)
        url =  reverse('users_universidad-detail', kwargs={'pk': user_universidad.pk})
        universidad_data = {
            'name': 'Setenal',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        universidad=Universidad.objects.create(**universidad_data)
        user_universidad_data = {
            'universidad': universidad.id,
            'user': user.id,
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.put(url, user_universidad_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        user_universidad.refresh_from_db()
        self.assertEqual(user_universidad.universidad.id, user_universidad_data['universidad'])

    def test_delete_users_universidad(self):
        universidad_data = {
            'name': 'Setenal',
            'rfc': '555-1234',
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        universidad=Universidad.objects.create(**universidad_data)
        user_data = {
            "name": "Rafael",
            "last_name_1": "Hernandez",
            "last_name_2": "Espinosa",
            "email": "rafa@setenal.mx",
            "password": "jesco814",
            "preferred_language": "en"
        }
        user=Users.objects.create(**user_data)
        user_universidad_data = {
            'universidad': universidad,
            'user': user,
            'created_by_id': self.user.id,
            'updated_by_id': self.user.id,
        }
        user_universidad=UsersUniversidad.objects.create(**user_universidad_data)
        url =  reverse('users_universidad-detail', kwargs={'pk': user_universidad.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(UsersUniversidad.objects.count(), 0)