from django.conf import settings
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.viewsets.dataset.service import DatasetService
from api.viewsets.image.service import ImageService
from api.viewsets.image_labels.service import ImageLabelsService
from api.viewsets.training.model import Training
from api.viewsets.training.serializer import TrainingSerializer
from api.viewsets.training.service import TrainingService
from core.services.rabbitmq_producer import RabbitMQProducer


class TrainingViewSet(mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Training.objects.all()

    serializer_class = TrainingSerializer

    training_service = TrainingService()

    def retrieve(self, request, *args, **kwargs):
        dataset = kwargs['pk']
        if request.user.role == 'ADMIN' and request.user.company:
            trainings = self.training_service.get_trainings_by_dataset(dataset)
        else:
            trainings = self.training_service.get_trainings_by_dataset_and_user(dataset, request.user)
        json_trainings = self.get_serializer(trainings, many=True).data
        trainings_to_return = self.training_service.format_trainings(json_trainings, dataset)
        return Response(trainings_to_return, status=status.HTTP_200_OK)

    @action(methods=["post"], name="mark_to_train", url_path="mark-to-train", url_name="mark-to-train", detail=False,
            permission_classes=[IsAuthenticated])
    def mark_to_train(self, request):
        training = {"dataset": request.data["dataset"], "user": request.user.uuid}
        ImageService().update_mark_to_train_at()
        ImageLabelsService().update_mark_to_train_at()
        self.training_service.create(training)
        return Response(status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        project = DatasetService().get_project(request.data["dataset"])
        rabbit_config = {"user": settings.RABBITMQ_USER, "password": settings.RABBITMQ_PASSWORD,
                         "host": settings.RABBITMQ_HOST, "vhost": settings.RABBITMQ_VHOST,
                         "queue_name": settings.RABBITMQ_QUEUE_NAME}
        mq_producer = RabbitMQProducer(rabbit_config)
        mq_producer.publish_message({"dataset": request.data["dataset"],
                                     "path": f"{project.storage_in}/{project.uuid}"})
        return Response(status=status.HTTP_200_OK)
