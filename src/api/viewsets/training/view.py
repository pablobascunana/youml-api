from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from api.viewsets.image.service import ImageService
from api.viewsets.image_labels.service import ImageLabelsService
from api.viewsets.training.model import Training
from api.viewsets.training.serializer import TrainingSerializer
from api.viewsets.training.service import TrainingService


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

    def create(self, request, *args, **kwargs):
        training = {"dataset": request.data['dataset'], "user": request.user.uuid}
        ImageService().update_mark_to_train_at()
        ImageLabelsService().update_mark_to_train_at()
        self.training_service.create(training)
        return Response(status=status.HTTP_200_OK)
