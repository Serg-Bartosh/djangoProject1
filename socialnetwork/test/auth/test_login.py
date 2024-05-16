from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_302_FOUND, HTTP_403_FORBIDDEN

from socialnetwork.models import User
from socialnetwork.serializers.auth.login import LoginSerializer


class LoginTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(first_name='John', last_name='Doe', username='johndoe',
                                        email='johndoe@admin.com',
                                        password='johndoejohndoe')
        self.request_data = {'email': 'johndoe@admin.com',
                             'password': 'johndoejohndoe'}
        self.url = reverse('login')

    def test_user_is_auth(self):
        self.client.force_login(self.user)
        serializer = LoginSerializer(data=self.request_data)
        self.assertTrue(serializer.is_valid())
        response = self.client.post(self.url, data=serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)
        self.assertIn('_auth_user_id', self.client.session)

    # TODO: написать проверку правильности пароля
    # def test_data_is_valid(self):
    #     serializer = LoginSerializer(data=self.request_data)
    #     self.assertTrue(serializer.is_valid())
    #     response = self.client.post(self.url, data=serializer.validated_data)
    #     self.assertEqual(response.status_code, HTTP_302_FOUND)
    #     self.assertTrue(self.user.is_authenticated)
    #     self.assertRedirects(response, expected_url=reverse('profile', kwargs={'username': 'johndoe'}))

    def test_email_is_not_valid(self):
        self.request_data['email'] = 'johndoe'
        serializer = LoginSerializer(data=self.request_data)
        self.assertFalse(serializer.is_valid())
        response = self.client.post(self.url, data=serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_password_is_not_valid(self):
        self.request_data['password'] *= 100
        serializer = LoginSerializer(data=self.request_data)
        self.assertFalse(serializer.is_valid())
        response = self.client.post(self.url, data=serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_user_no_create(self):
        self.request_data['email'] = 'userthatdoesntcreate@admin.com'
        self.request_data['password'] = 'safepassword'
        serializer = LoginSerializer(data=self.request_data)
        self.assertTrue(serializer.is_valid())
        response = self.client.post(self.url, data=serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertNotIn('_auth_user_id', self.client.session)
