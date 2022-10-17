from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response

from api.viewsets.company.model import Company
from api.viewsets.company.serializer import CompanySerializer
from api.viewsets.company.service import CompanyService
from core.services.email import EmailService
from core.utils.file import replace_keys
from core.permissions import IsAllowed
from users.viewsets.user.service import RegisterUserService


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAllowed]

    @staticmethod
    def list(request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    @staticmethod
    def create(request, *args, **kwargs):
        created_company = CompanyService.create_company(request.data['company'])
        user = request.data['user']
        user['company'] = created_company
        token = RegisterUserService().create_company_user(user)
        email_service = EmailService()
        body = email_service.get_template(f"{settings.BASE_DIR}/templates/account_verification.html")
        body = replace_keys(body, '##VERIFICATION_TOKEN##', token)
        return email_service.send_sendgrid_email(receiver_email=request.data['user']['email'],
                                                 subject='youML - Account verification', body=body)
