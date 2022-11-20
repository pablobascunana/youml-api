from typing import Dict

from api.viewsets import Training
from api.viewsets.training.serializer import TrainingSerializer
from users.models import User


class TrainingService:

    @staticmethod
    def create(training: Dict):
        image_serializer = TrainingSerializer(data=training)
        image_serializer.is_valid(raise_exception=True)
        return Training.objects.create(**image_serializer.validated_data)

    @staticmethod
    def get_trainings_by_dataset(dataset: str) -> Training:
        return Training.objects.filter(dataset=dataset)

    @staticmethod
    def get_trainings_by_dataset_and_user(dataset: str, user: User) -> Training:
        return Training.objects.filter(dataset=dataset, user=user)
