from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from socialnetwork.views.article.comment import CommentArticleView
from socialnetwork.views.article.likes import LikeArticleView
from socialnetwork.views.main import MainView
from socialnetwork.views.profile.profile import ProfileView
from socialnetwork.views.profile.article import ArticleView
from socialnetwork.views.auth.registration import RegistrationView
from socialnetwork.views.auth.login import LoginView
from socialnetwork.views.auth.singout import LogoutView
from socialnetwork.views.profile.photo import ProfilePhotoView
from socialnetwork.views.article.article import ArticlePageView
from socialnetwork.views.search_user import SearchView

urlpatterns = [
                  path('main/', MainView.as_view(), name='main'),
                  path('main/profile/<str:username>/', ProfileView.as_view(), name='profile'),
                  path('profile/registration', RegistrationView.as_view(), name='registration'),
                  path('profile/login', LoginView.as_view(), name='login'),
                  path('profile/logout', LogoutView.as_view(), name='logout'),
                  path('profile/photo', ProfilePhotoView.as_view(), name='photo'),
                  path('profile/article', ArticleView.as_view(), name='article'),
                  path('article/<str:author>/<str:title>/', ArticlePageView.as_view(), name='article_page'),
                  path('article/<str:author>/<str:title>/artecle_add_comment', CommentArticleView.as_view(),
                       name='article_add_comment'),
                  path('article/<str:author>/<str:title>/artecle_like', LikeArticleView.as_view(),
                       name='article_like'),
                  path('search/<str:username>/', SearchView.as_view(), name='search'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
