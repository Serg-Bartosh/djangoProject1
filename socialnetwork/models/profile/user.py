from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from socialnetwork.validator.user.card_number_validator import card_number_validator


class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, blank=False)
    card_number = models.CharField(max_length=19, blank=True, null=True, unique=True,
                                   validators=[card_number_validator])
    card_expiry_date = models.DateField(blank=True, null=True)
    card_holder_name = models.CharField(max_length=255, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()
