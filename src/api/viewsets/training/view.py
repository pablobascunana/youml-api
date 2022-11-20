from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from api.viewsets.image.service import ImageService
from api.viewsets.image_labels.service import ImageLabelService
from api.viewsets.training.model import Training
from api.viewsets.training.serializer import TrainingSerializer
from api.viewsets.training.service import TrainingService


class TrainingViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Training.objects.all()

    serializer_class = TrainingSerializer

    def create(self, request, *args, **kwargs):
        training = {"dataset": request.data['dataset'], "user": request.user.uuid}
        ImageService().update_mark_to_train_at()
        ImageLabelService().update_mark_to_train_at()
        TrainingService().create(training)
        return Response(status=status.HTTP_200_OK)
