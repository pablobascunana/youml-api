import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from api.mixins.validate_model import ValidateModelMixin
from api.viewsets.dataset.model import Dataset


class Image(ValidateModelMixin, models.Model):
    uuid = models.UUIDField(_('uuid'), max_length=64, unique=True, primary_key=True, default=uuid.uuid4)
    name = models.CharField(_('name'), max_length=30, null=False)
    path = models.CharField(_('path'), max_length=30, null=False)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, null=False, blank=False, db_column='dataset')

    REQUIRED_FIELDS = ['dataset', 'name', 'path']

    class Meta:
        db_table = 'image'
        unique_together = ('dataset', 'name')
