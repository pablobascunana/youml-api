from django.db.models import QuerySet

from api.viewsets import Label


class LabelService:

    @staticmethod
    def get_labels_by_dataset(dataset: str) -> QuerySet:
        return Label.objects.filter(dataset=dataset)
