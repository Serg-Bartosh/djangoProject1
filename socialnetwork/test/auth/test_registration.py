from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_302_FOUND, HTTP_403_FORBIDDEN

from socialnetwork.models import User
from socialnetwork.serializers.auth.registration import RegistrationSerializer


class RegistrationTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.request_data = {'first_name': 'John', 'last_name': 'Doe', 'username': 'johndoe',
                             'email': 'johndoe@admin.com',
                             'password': 'johndoejohndoe'}

    def test_data_is_valid(self):
        serializer = RegistrationSerializer(data=self.request_data)
        self.assertTrue(serializer.is_valid())
        response = self.client.post(reverse('registration'), serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_302_FOUND)
        user = User.objects.get(username=serializer.validated_data['username'])
        self.assertTrue(user.is_authenticated)
        self.assertRedirects(response, expected_url=reverse('profile', kwargs={'username': 'johndoe'}))

    def test_email_is_not_valid(self):
        self.request_data['email'] = 'asdsadadas'
        serializer = RegistrationSerializer(data=self.request_data)
        self.assertFalse(serializer.is_valid())
        response = self.client.post(reverse('registration'), serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_password_is_not_valid(self):
        self.request_data['password'] *= 100
        serializer = RegistrationSerializer(data=self.request_data)
        self.assertFalse(serializer.is_valid())
        response = self.client.post(reverse('registration'), serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_first_name_is_not_valid(self):
        self.request_data['first_name'] *= 100
        serializer = RegistrationSerializer(data=self.request_data)
        self.assertFalse(serializer.is_valid())
        response = self.client.post(reverse('registration'), serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_last_name_is_not_valid(self):
        self.request_data['last_name'] *= 100
        serializer = RegistrationSerializer(data=self.request_data)
        self.assertFalse(serializer.is_valid())
        response = self.client.post(reverse('registration'), serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_username_is_not_valid(self):
        self.request_data['username'] *= 100
        serializer = RegistrationSerializer(data=self.request_data)
        self.assertFalse(serializer.is_valid())
        response = self.client.post(reverse('registration'), serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_data_is_empty(self):
        self.request_data = {'first_name': '', 'last_name': '', 'username': '',
                             'email': '',
                             'password': ''}
        serializer = RegistrationSerializer(data=self.request_data)
        self.assertFalse(serializer.is_valid())
        response = self.client.post(reverse('registration'), serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_data_is_not_valid(self):
        self.request_data = {'first_name': 'John' * 100, 'last_name': 'Doe' * 100, 'username': 'johndoe' * 100,
                             'email': 'johndoe@admin.com' * 10,
                             'password': 'johndoejohndoe' * 10}
        serializer = RegistrationSerializer(data=self.request_data)
        self.assertFalse(serializer.is_valid())
        response = self.client.post(reverse('registration'), serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_user_is_auth(self):
        serializer = RegistrationSerializer(data=self.request_data)
        user = User.objects.create(first_name='John', last_name='Doe', username='johndoe',
                                   email='johndoe@admin.com',
                                   password='johndoejohndoe')
        self.client.force_authenticate(user)
        self.assertFalse(serializer.is_valid())
        response = self.client.post(reverse('registration'), serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_user_is_exist(self):
        serializer = RegistrationSerializer(data=self.request_data)
        User.objects.create(first_name='John', last_name='Doe', username='johndoe',
                            email='johndoe@admin.com',
                            password='johndoejohndoe')
        self.assertFalse(serializer.is_valid())
        response = self.client.post(reverse('registration'), serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
