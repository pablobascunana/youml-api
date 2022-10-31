from typing import Dict

from rest_framework import serializers

from api.viewsets.dataset.model import Dataset
from api.viewsets.dataset.serializer import DatasetSerializer


class DatasetService:

    @staticmethod
    def create(dataset: Dict) -> Dict:
        dataset_serializer = DatasetSerializer(data=dataset)
        dataset_serializer.is_valid(raise_exception=True)
        try:
            dataset_serializer.save()
        except Exception as e:
            raise serializers.ValidationError(e) from e
        return dataset_serializer.data

    @staticmethod
    def delete(dataset_uuid: str):
        return Dataset.objects.filter(pk=dataset_uuid).delete()[0]
