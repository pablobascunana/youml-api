from django.db.models import QuerySet

from api.viewsets import ImageLabels


class ImageLabelService:

    @staticmethod
    def filter_by_label_id(uuid: str) -> QuerySet:
        return ImageLabels.objects.filter(label=uuid)
