from typing import Dict

from api.viewsets import Dataset
from api.viewsets.dataset.serializer import DatasetSerializer


class DatasetService:

    @staticmethod
    def create(dataset: Dict) -> Dict:
        dataset_serializer = DatasetSerializer(data=dataset)
        dataset_serializer.is_valid(raise_exception=True)
        dataset_serializer.save()
        return dataset_serializer.data

    @staticmethod
    def delete(dataset_uuid: str):
        return Dataset.objects.filter(pk=dataset_uuid).delete()[0]
