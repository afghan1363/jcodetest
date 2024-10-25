from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name=_("Email"))
    full_name = models.CharField(max_length=150, verbose_name=_("Full name"))
    phone = PhoneNumberField(unique=True, verbose_name=_('Phone'))

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.full_name}'
