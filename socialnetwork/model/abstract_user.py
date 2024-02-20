from django.contrib.auth.models import AbstractUser
from django.db import models

from .user_manager import UserManager


class User(AbstractUser):
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    user_name = models.CharField(max_length=255, blank=False, unique=True)
    email = models.EmailField(max_length=255, unique=True, blank=False)
    password = models.CharField(max_length=255, blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'user_name', 'email', 'password'

    objects = UserManager()
