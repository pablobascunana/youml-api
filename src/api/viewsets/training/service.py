from typing import Dict

from django.db.models import QuerySet

from api.viewsets import Training
from api.viewsets.image.service import ImageService
from api.viewsets.image_labels.service import ImageLabelsService
from api.viewsets.label.services import LabelService
from api.viewsets.training.serializer import TrainingSerializer
from core.utils.date import str_date_to_db_datetime
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

    def format_trainings(self, trainings: Dict, dataset: str) -> Dict:
        for training in trainings:
            created_at = str_date_to_db_datetime(training['created_at'])
            training['images'] = ImageService.get_images_count_by_dataset_and_date(dataset, created_at)
            labels = LabelService().get_labels_by_dataset(dataset)
            training['labels'] = self.format_labels(labels, created_at)
        return trainings

    @staticmethod
    def format_labels(labels: QuerySet, created_at: str) -> Dict:
        training_dict = {}
        for label in labels:
            current_labels = ImageLabelsService.get_image_labels_count_by_dataset_and_date(label, created_at)
            if current_labels > 0:
                training_dict[label.name] = current_labels
        return training_dict
