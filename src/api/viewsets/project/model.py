import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from api.mixins.validate_model import ValidateModelMixin
from core.utils.date import date_now


class Project(ValidateModelMixin, models.Model):
    uuid = models.UUIDField(_('uuid'), max_length=64, unique=True, primary_key=True, default=uuid.uuid4)
    name = models.CharField(_('name'), max_length=30, null=False, blank=False)
    created_at = models.DateTimeField(_('createdAt'), default=date_now(), db_column='createdAt')
    storage_in = models.CharField(_('storageIn'), max_length=240, null=False, blank=False, db_column='storageIn')
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=False, blank=False, db_column='user')

    REQUIRED_FIELDS = ['user', 'name', 'storage_in']

    class Meta:
        db_table = 'project'
        unique_together = ('user', 'name')
