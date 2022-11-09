import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from api.mixins.validate_model import ValidateModelMixin
from api.viewsets import Label, Image


class ImageLabels(ValidateModelMixin, models.Model):
    uuid = models.UUIDField(_('uuid'), max_length=64, unique=True, primary_key=True, default=uuid.uuid4)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, null=False, blank=False, db_column='image')
    label = models.ForeignKey(Label, on_delete=models.CASCADE, null=False, blank=False, db_column='label')
    mark_to_train_at = models.DateTimeField(_('markToTrainAt'), null=True, blank=True, db_column='markToTrainAt')

    REQUIRED_FIELDS = ['image', 'label']

    class Meta:
        db_table = 'image_labels'
