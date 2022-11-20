from typing import Dict

from api.viewsets import Training
from api.viewsets.training.serializer import TrainingSerializer


class TrainingService:

    @staticmethod
    def create(training: Dict):
        image_serializer = TrainingSerializer(data=training)
        image_serializer.is_valid(raise_exception=True)
        return Training.objects.create(**image_serializer.validated_data)
