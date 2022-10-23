import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from api.mixins.validate_model import ValidateModelMixin
from api.viewsets.project.model import Project


class Dataset(ValidateModelMixin, models.Model):
    uuid = models.UUIDField(_('uuid'), max_length=64, unique=True, primary_key=True, default=uuid.uuid4)
    name = models.CharField(_('name'), max_length=30, null=False)
    created_at = models.DateTimeField(_('createdAt'), default=timezone.now, db_column='createdAt')
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, null=False, blank=False, db_column='user')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=False, blank=False, db_column='project')

    REQUIRED_FIELDS = ['uuid', 'user', 'project', 'name']

    class Meta:
        db_table = 'dataset'
        unique_together = ('user', 'name')
