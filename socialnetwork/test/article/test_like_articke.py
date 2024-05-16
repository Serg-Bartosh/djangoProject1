# from os import path
#
# from rest_framework.test import APITestCase, APIClient
# from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_302_FOUND, HTTP_403_FORBIDDEN, HTTP_200_OK
#
# from django.core.files.uploadedfile import SimpleUploadedFile
# from django.urls import reverse
#
# from socialnetwork.models import User, Article, ArticleLike
#
# from socialnetwork.serializers.article.like import LikeArticleSerializer
#
# image_path = path.join(path.dirname(__file__), '../data_for_test/images /test_image.png')
# with open(image_path, 'rb') as f:
#     image_content = f.read()
#
#
# # TODO: сделать нормальную проверку + обновить обновление лайков
# class LikeOrDislikeArticleTestCase(APITestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create(first_name='John', last_name='Doe', username='johndoe',
#                                         email='johndoe@admin.com',
#                                         password='johndoejohndoe')
#         self.image = SimpleUploadedFile(name='test_image.png', content=image_content,
#                                         content_type='image/png')
#         self.article = Article.objects.create(author=self.user, image=self.image,
#                                               title='I am good guy',
#                                               content='U thought that i will proof it?')
#         self.request_data = {'like': True}
#         self.url = reverse('article_like', kwargs={'author': self.user.id, 'title': 'I am good guy'})
#
#     def test_data_is_valid(self):
#         self.client.force_login(self.user)
#         serializer = LikeArticleSerializer(data=self.request_data)
#         self.assertTrue(serializer.is_valid(), serializer.errors)
#         response = self.client.post(self.url, data=serializer.validated_data)
#         self.assertEqual(response.status_code, HTTP_200_OK)
#
#     # TODO: переводит текст в буль , так не должно быть
#     def test_data_not_valid(self):
#         self.client.force_login(self.user)
#         self.request_data = {'like': 'asdasd'}
#         serializer = LikeArticleSerializer(data=self.request_data)
#         self.assertFalse(serializer.is_valid(), serializer.errors)
#         response = self.client.post(self.url, data=serializer.validated_data)
#         self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
#
#     def test_user_is_not_auth(self):
#         serializer = LikeArticleSerializer(data=self.request_data)
#         self.assertTrue(serializer.is_valid(), serializer.errors)
#         response = self.client.post(self.url, data=serializer.validated_data)
#         self.assertEqual(response.status_code, HTTP_403_FORBIDDEN)
#
#     def test_change_state_like(self):
#         self.client.force_login(self.user)
#         serializer_true = LikeArticleSerializer(data=self.request_data)
#         self.assertTrue(serializer_true.is_valid(), serializer_true.errors)
#         response_true = self.client.post(self.url, data=serializer_true.validated_data)
#         self.assertEqual(response_true.status_code, HTTP_200_OK)
#         self.assertEqual(ArticleLike.objects.get(user=self.user, article=self.article).like, True)
#         self.request_data = {'like': False}
#         serializer_false = LikeArticleSerializer(data=self.request_data)
#         self.assertTrue(serializer_false.is_valid(), serializer_false.errors)
#         response_false = self.client.post(self.url, data=serializer_false.validated_data)
#         self.assertEqual(response_false.status_code, HTTP_200_OK)
#         self.assertEqual(ArticleLike.objects.get(user=self.user, article=self.article).like, False)
