from rest_framework import viewsets, status
from rest_framework.response import Response

from core.services.email import EmailService
from core.utils.file import read_file
from users.models import User
from users.viewsets.user.permissions import IsAllowed
from users.viewsets.user.serializer import UserSerializer
from users.viewsets.user.service import UserService
from django.conf import settings


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAllowed]

    @staticmethod
    def list(request, *args, **kwargs):
        # TODO FUTURE, maybe it is possible to return all user list if the request is requested by an admin user
        return Response(status=status.HTTP_403_FORBIDDEN)

    @staticmethod
    def create(request, *args, **kwargs):
        UserService.create_user(request.data)
        body = read_file(f"{settings.BASE_DIR}/templates/account_verification.html")
        email_service = EmailService()
        return email_service.send_sendgrid_email(receiver_email=request.data['email'],
                                                 subject='youML - Account verification', body=body)
