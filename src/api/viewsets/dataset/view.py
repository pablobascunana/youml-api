from rest_framework import viewsets, status
from rest_framework.response import Response

from api.viewsets.dataset.model import Dataset
from api.viewsets.dataset.serializer import DatasetSerializer
from api.viewsets.dataset.service import DatasetService


class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    @staticmethod
    def create(request, *args, **kwargs):
        dataset = {'name': request.data['name'], 'user': request.user.uuid, 'project': request.data['project']}
        created_dataset = DatasetService().create_dataset(dataset)
        return Response(created_dataset, status=status.HTTP_201_CREATED)
