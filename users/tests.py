from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Users
from rest_framework_simplejwt.tokens import AccessToken

class UserManagementViewTests(APITestCase):

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

    def test_create_user(self):
        url = reverse('users-list')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        user_data = {
                    "name": "Rafael",
                    "last_name_1": "Hernandez",
                    "last_name_2": "Espinosa",
                    "email": "rafa@setenal.mx",
                    "password": "jesco814",
                    "preferred_language": "en"
        }
        response = self.client.post(url, user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Users.objects.count(), 2)

    def test_get_user_list(self):
        url = reverse('users-list')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user(self):
        url = reverse('users-detail', args=[self.user.id])
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user(self):
        url = reverse('users-detail', args=[self.user.id])
        updated_data = {
            "name": "Rafael",
            "last_name_1": "Hernandez",
            "email": "rafaw@setenal.mx",
            "password": "jesco814",
            "preferred_language": "en"
        }
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.user.refresh_from_db()
        self.assertEqual(self.user.name, updated_data['name'])
        self.assertEqual(self.user.email, updated_data['email'])
        self.assertEqual(self.user.preferred_language, updated_data['preferred_language'])

    def test_delete_user(self):
        self.user.is_superuser = True
        self.user.save()
        url = reverse('users-detail', args=[self.user.id])
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Users.objects.filter(id=self.user.id, deleted=False).exists())
