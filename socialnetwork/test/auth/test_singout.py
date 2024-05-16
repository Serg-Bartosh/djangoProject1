from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_302_FOUND, HTTP_403_FORBIDDEN

from socialnetwork.models import User
from socialnetwork.serializers.auth.login import LoginSerializer


class SingOutTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(first_name='John', last_name='Doe', username='johndoe',
                                        email='johndoe@admin.com',
                                        password='johndoejohndoe')
        self.url = reverse('logout')

    def test_user_is_auth(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTP_302_FOUND)
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_user_is_not_auth(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)
        self.assertNotIn('_auth_user_id', self.client.session)
