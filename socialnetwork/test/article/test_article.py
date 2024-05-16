from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN, HTTP_200_OK

from socialnetwork.models import User
from socialnetwork.serializers.profile.article import ArticleSerializer

from django.core.files.uploadedfile import SimpleUploadedFile
import os

image_path = os.path.join(os.path.dirname(__file__), '../data_for_test/images /test_image.png')
with open(image_path, 'rb') as f:
    image_content = f.read()


class CreateArticleTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(first_name='John', last_name='Doe', username='johndoe',
                                        email='johndoe@admin.com',
                                        password='johndoejohndoe')
        self.image = SimpleUploadedFile(name='test_image.png', content=image_content,
                                        content_type='image/png')
        self.request_data = {'image': self.image,
                             'title': 'I am good guy',
                             'content': 'U thought that i will proof it?'}
        self.url = reverse('article')

    def test_data_is_valid(self):
        self.client.force_login(self.user)
        serializer = ArticleSerializer(data=self.request_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        response = self.client.post(self.url, data=serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_image_is_empty(self):
        self.client.force_login(self.user)
        self.request_data['image'] = None
        serializer = ArticleSerializer(data=self.request_data)
        self.assertFalse(serializer.is_valid(), serializer.errors)
        response = self.client.post(self.url, data=serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_title_is_empty(self):
        self.client.force_login(self.user)
        self.request_data['title'] = None
        serializer = ArticleSerializer(data=self.request_data)
        self.assertFalse(serializer.is_valid(), serializer.errors)
        response = self.client.post(self.url, data=serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_content_is_empty(self):
        self.client.force_login(self.user)
        self.request_data['content'] = None
        serializer = ArticleSerializer(data=self.request_data)
        self.assertFalse(serializer.is_valid(), serializer.errors)
        response = self.client.post(self.url, data=serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_data_is_empty(self):
        self.client.force_login(self.user)
        self.request_data['image'] = None
        self.request_data['title'] = None
        self.request_data['content'] = None
        serializer = ArticleSerializer(data=self.request_data)
        self.assertFalse(serializer.is_valid(), serializer.errors)
        response = self.client.post(self.url, data=serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_data_is_not_valid(self):
        self.client.force_login(self.user)
        self.request_data['image'] = 'adasd'
        self.request_data['title'] = self.image
        self.request_data['content'] = self.image
        serializer = ArticleSerializer(data=self.request_data)
        self.assertFalse(serializer.is_valid(), serializer.errors)
        response = self.client.post(self.url, data=serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_user_not_auth_data_is_valid(self):
        serializer = ArticleSerializer(data=self.request_data)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        response = self.client.post(self.url, data=serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)

    def test_user_not_auth_data_is_not_valid(self):
        self.request_data['image'] = 'adasd'
        self.request_data['title'] = self.image
        self.request_data['content'] = self.image
        serializer = ArticleSerializer(data=self.request_data)
        self.assertFalse(serializer.is_valid(), serializer.errors)
        response = self.client.post(self.url, data=serializer.validated_data)
        self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)
