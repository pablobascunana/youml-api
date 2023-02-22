from rest_framework import viewsets, status, mixins
from rest_framework.response import Response

from api.viewsets.dataset.model import Dataset
from api.viewsets.dataset.serializer import DatasetSerializer
from api.viewsets.dataset.service import DatasetService
from users.viewsets.user.service import RegisterUserService


class DatasetViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    dataset_service = DatasetService()

    def list(self, request, *args, **kwargs):
        if request.user.role == 'ADMIN' and request.user.company:
            users = RegisterUserService().get_users_by_company_id(request.user.company_id)
            datasets = self.get_queryset().filter(user__in=users.values('uuid'), project=request.GET.get('project'))
        else:
            datasets = self.get_queryset().filter(user=request.user, project=request.GET.get('project'))

        json_datasets = self.get_serializer(datasets, many=True).data
        return Response(json_datasets, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        dataset = {'name': request.data['name'], 'user': request.user.uuid, 'project': request.data['project']}
        created_dataset = self.dataset_service.create(dataset)
        return Response(created_dataset, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None, *args, **kwargs):
        destroyed = self.dataset_service.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT) if destroyed > 0 \
            else Response("Resource not found", status=status.HTTP_404_NOT_FOUND)
