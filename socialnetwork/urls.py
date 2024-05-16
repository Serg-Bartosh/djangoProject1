from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from socialnetwork.consumer import ChatConsumer
from socialnetwork.views.article.comment import CommentArticleView
from socialnetwork.views.article.likes import LikeArticleView
from socialnetwork.views.chat import ChatViewSet, UserChatViewSet
from socialnetwork.views.main import MainView
from socialnetwork.views.payments.donate import DonateView
from socialnetwork.views.payments.payment import PaymentView
from socialnetwork.views.profile.avatar import AvatarView
from socialnetwork.views.profile.profile import ProfileView
from socialnetwork.views.profile.article import ArticleView
from socialnetwork.views.auth.registration import RegistrationView
from socialnetwork.views.auth.login import LoginView
from socialnetwork.views.auth.singout import LogoutView
from socialnetwork.views.profile.photo import ProfilePhotoView
from socialnetwork.views.article.article import ArticlePageView
from socialnetwork.views.main.search_user import SearchUserViewSet

urlpatterns = [
                  path('main/', MainView.as_view(), name='main'),
                  path('main/profile/<str:username>/', ProfileView.as_view(), name='profile'),
                  path('auth/registration', RegistrationView.as_view(), name='registration'),
                  path('auth/login', LoginView.as_view(), name='login'),
                  path('auth/logout', LogoutView.as_view(), name='logout'),
                  path('profile/<str:username>/photo', ProfilePhotoView.as_view(), name='photo'),
                  path('profile/article', ArticleView.as_view(), name='article'),
                  path('profile/<str:username>/avatar', AvatarView.as_view(), name='avatar'),
                  path('article/<str:author>/<str:title>/', ArticlePageView.as_view(), name='article_page'),
                  path('article/<str:author>/<str:title>/artecle_add_comment', CommentArticleView.as_view(),
                       name='article_add_comment'),
                  path('article/<str:author>/<str:title>/artecle_like', LikeArticleView.as_view(),
                       name='article_like'),
                  path('main/search/<str:user_inf>/', SearchUserViewSet.as_view({'get': 'list'}), name='search'),
                  path('main/chat/<int:user_id>/', ChatViewSet.as_view({'get': 'list'}), name='chat'),
                  path('main/user/chats/', UserChatViewSet.as_view({'get': 'list'}), name='user_chat'),
                  path('main/donate/', DonateView.as_view(), name='donate'),
                  path('main/donate/paymants/', PaymentView.as_view(), name='payment'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

websocket_urlpatterns = [
    path('main/ws/chat/<int:user_id>/', ChatConsumer.as_asgi(), name='chat'),
]
