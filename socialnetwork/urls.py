from django.urls import path
from socialnetwork.views.main import MainView
from socialnetwork.views.profile import ProfileView
from socialnetwork.views.registration import RegistrationView
from socialnetwork.views.login import LoginView
from socialnetwork.views.singout import LogoutView

urlpatterns = [
    path('main/', MainView.as_view(), name='main'),
    path('main/profile', ProfileView.as_view(), name='profile'),
    path('profile/registration', RegistrationView.as_view(), name='registration'),
    path('profile/login', LoginView.as_view(), name='login'),
    path('profile/logout', LogoutView.as_view(), name='logout'),
]
