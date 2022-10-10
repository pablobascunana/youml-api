from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response

from api.viewsets.company.model import Company
from api.viewsets.company.serializer import CompanySerializer
from api.viewsets.company.service import CompanyService
from core.services.email import EmailService
from core.utils.file import replace_keys
from users.viewsets.user.permissions import IsAllowed
from users.viewsets.user.service import RegisterUserService


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
        user = request.data['user']
        created_company = CompanyService.create_company(request.data['company'])
        user['company_uuid'] = created_company['uuid']
        created_user, token = RegisterUserService().create_company_user(user)
        email_service = EmailService()
        body = email_service.get_template(f"{settings.BASE_DIR}/templates/account_verification.html")
        body = replace_keys(body, '##VERIFICATION_TOKEN##', token)
        body = replace_keys(body, '##USER_UUID##', str(created_user.uuid))
        return email_service.send_sendgrid_email(receiver_email=request.data['user']['email'],
                                                 subject='youML - Account verification', body=body)
