from rest_framework import viewsets, status
from rest_framework.response import Response

from api.viewsets.dataset.model import Dataset
from api.viewsets.dataset.serializer import DatasetSerializer
from api.viewsets.dataset.service import DatasetService
from users.viewsets.user.service import RegisterUserService


class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

    def list(self, request, *args, **kwargs):
        if request.user.role == 'ADMIN' and request.user.company:
            users = RegisterUserService().get_users_by_company_id(request.user.company_id)
            datasets = self.get_queryset().filter(user__in=users.values('uuid'), project=request.GET.get('project'))
        else:
            datasets = self.get_queryset().filter(user=request.user, project=request.GET.get('project'))

        json_datasets = DatasetSerializer(datasets, many=True).data
        return Response(json_datasets, status=status.HTTP_200_OK)

    @staticmethod
    def create(request, *args, **kwargs):
        dataset = {'name': request.data['name'], 'user': request.user.uuid, 'project': request.data['project']}
        created_dataset = DatasetService().create_dataset(dataset)
        return Response(created_dataset, status=status.HTTP_201_CREATED)
