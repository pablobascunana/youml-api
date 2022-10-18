from typing import Dict

from api.viewsets.dataset.serializer import DatasetSerializer


class DatasetService:

    @staticmethod
    def create_dataset(dataset: Dict) -> Dict:
        dataset_serializer = DatasetSerializer(data=dataset)
        dataset_serializer.is_valid(raise_exception=True)
        dataset_serializer.save()
        return dataset_serializer.data
