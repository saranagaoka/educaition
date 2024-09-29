from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser

from base.fields import LowercaseEmailField
from users.managers import UserManager


class User(AbstractUser):
    email = LowercaseEmailField(verbose_name='Adres e-mail', null=True, unique=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
