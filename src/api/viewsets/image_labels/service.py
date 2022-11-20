from django.db.models import QuerySet

from core.utils.query import do_bulk_update
from api.viewsets import ImageLabels


class ImageLabelService:

    @staticmethod
    def filter_by_label_id(uuid: str) -> QuerySet:
        return ImageLabels.objects.filter(label=uuid)

    @staticmethod
    def get_mark_to_train_at_with_value_none():
        return ImageLabels.objects.filter(mark_to_train_at__isnull=True)

    def update_mark_to_train_at(self):
        image_labels = self.get_mark_to_train_at_with_value_none()
        do_bulk_update(image_labels, ImageLabels, ['mark_to_train_at'])
