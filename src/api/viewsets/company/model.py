import uuid

from django.core.validators import EmailValidator
from django.db import models

from django.utils.translation import gettext_lazy as _

from api.mixins.validate_model import ValidateModelMixin


class Company(ValidateModelMixin, models.Model):
    email_validator = EmailValidator()

    uuid = models.UUIDField(_('uuid'), max_length=64, unique=True, primary_key=True, default=uuid.uuid4)
    name = models.CharField(_('name'), max_length=30, null=False)
    cif = models.CharField(_('cif'), max_length=9, unique=True, null=False)
    email = models.EmailField(_('email'), max_length=80, unique=True, null=False, validators=[email_validator])
    address = models.CharField(_('address'), max_length=150)
    city = models.CharField(_('city'), max_length=24)
    country = models.CharField(_('country'), max_length=24)
    postal_code = models.PositiveSmallIntegerField(_('postal_code'))
    sector = models.CharField(_('sector'), max_length=80)
    creation_date = models.DateTimeField(_('creation_date'), auto_now_add=True, null=False)
    active = models.BooleanField(_('active'), default=False)

    REQUIRED_FIELDS = ['uuid', 'name', 'cif', 'email']

    class Meta:
        db_table = 'company'
        unique_together = ('uuid', 'email', 'name', 'cif')
