from rest_framework import viewsets, status
from rest_framework.response import Response

from api.viewsets.company.model import Company
from api.viewsets.company.serializer import CompanySerializer
from api.viewsets.company.service import CompanyService
from users.viewsets.user.permissions import IsAllowed
from users.viewsets.user.service import UserService


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAllowed]

    @staticmethod
    def list(request, *args, **kwargs):
        # TODO FUTURE, for now it is not possible to get anything for companies
        return Response(status=status.HTTP_403_FORBIDDEN)

    @staticmethod
    def create(request, *args, **kwargs):
        CompanyService.create_company(request.data['company'])
        UserService.create_user(request.data['user'])
        return Response({}, status=status.HTTP_201_CREATED)
