from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from api.viewsets.image.service import ImageService
from api.viewsets.image_labels.service import ImageLabelsService
from api.viewsets.label.services import LabelService
from api.viewsets.training.model import Training
from api.viewsets.training.serializer import TrainingSerializer
from api.viewsets.training.service import TrainingService
from core.utils.date import str_date_to_db_datetime


class TrainingViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Training.objects.all()

    serializer_class = TrainingSerializer

    training_service = TrainingService()
    image_service = ImageService()
    image_labels_service = ImageLabelsService()

    def retrieve(self, request, *args, **kwargs):
        dataset = kwargs['pk']
        if request.user.role == 'ADMIN' and request.user.company:
            trainings = self.training_service.get_trainings_by_dataset(dataset)
        else:
            trainings = self.training_service.get_trainings_by_dataset_and_user(dataset, request.user)
        json_trainings = self.get_serializer(trainings, many=True).data
        for training in json_trainings:
            created_at = str_date_to_db_datetime(training['created_at'])
            training['images'] = self.image_service.get_images_count_by_dataset_and_date(dataset, created_at)
            labels = LabelService().get_labels_by_dataset(dataset)
            training_dict = {}
            for label in labels:
                current_labels = self.image_labels_service.get_image_labels_count_by_dataset_and_date(label, created_at)
                if current_labels > 0:
                    training_dict[label.name] = current_labels
            training['labels'] = training_dict
        return Response(json_trainings, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        training = {"dataset": request.data['dataset'], "user": request.user.uuid}
        self.image_service.update_mark_to_train_at()
        self.image_labels_service.update_mark_to_train_at()
        self.training_service.create(training)
        return Response(status=status.HTTP_200_OK)
