import uuid

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import EmailValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.viewsets.user.repository import UserRepository


class User(AbstractBaseUser):
    class Roles(models.TextChoices):
        ADMIN = 'ADMIN'
        NORMAL = 'NORMAL'

    username_validator = UnicodeUsernameValidator()
    email_validator = EmailValidator()

    uuid = models.UUIDField(_('uuid'), max_length=64, unique=True, primary_key=True, default=uuid.uuid4())
    username = models.CharField(_('username'), max_length=30, unique=True, validators=[username_validator])
    name = models.CharField(_('name'), max_length=30, null=False)
    lastname = models.CharField(_('lastname'), max_length=30, null=False)
    email = models.EmailField(_('email'), max_length=80, unique=True, null=False, validators=[email_validator])
    password = models.CharField(_('password'), max_length=150, null=False)
    verified = models.BooleanField(_('verified'), default=False, null=False)
    active = models.PositiveSmallIntegerField(_('active'), default=0, null=False)
    role = models.CharField(_('role'), max_length=10, default=Roles.NORMAL, null=False)
    login_attempts = models.PositiveSmallIntegerField(_('login_attempts'), default=0, null=False)
    register_date = models.DateTimeField(_('register_date'), auto_now_add=True, null=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['name', 'lastname', 'email', 'password']

    objects = UserRepository()

    class Meta:
        db_table = 'users'
        unique_together = ('email', 'username', 'uuid')
