import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from api.mixins.validate_model import ValidateModelMixin
from api.viewsets import Dataset


class Training(ValidateModelMixin, models.Model):

    class Status(models.TextChoices):
        PENDING = 'PENDING'
        PROCESSING = 'PROCESSING'
        COMPLETED = 'COMPLETED'
        ERROR = 'ERROR'

    uuid = models.UUIDField(_('uuid'), max_length=64, unique=True, primary_key=True, default=uuid.uuid4)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE, null=False, blank=False, db_column='dataset')
    status = models.CharField(_('status'), max_length=10, default=Status.PENDING, null=False)
    created_at = models.DateTimeField(_('createdAt'), default=timezone.now, db_column='createdAt')

    REQUIRED_FIELDS = ['dataset']
