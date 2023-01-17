from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from core.services.email import EmailService
from core.services.jwt import JwtToken
from core.utils.file import replace_keys
from users.models import User
from core.permissions import IsAllowed
from users.viewsets.user.serializer import UserSerializer
from users.viewsets.user.service import RegisterUserService
from django.conf import settings


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAllowed]

    user_service = RegisterUserService()

    @staticmethod
    def list(request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        token = self.user_service.create_user(request.data)
        email_service = EmailService()
        body = email_service.get_template(f"{settings.BASE_DIR}/templates/account_verification.html")
        body = replace_keys(body, '##VERIFICATION_TOKEN##', token)
        return email_service.send_sendgrid_email(receiver_email=request.data['email'],
                                                 subject='youML - Account verification', body=body)

    @action(methods=["get"], name="User validation", url_path='validate', url_name="Validate email user", detail=False,
            permission_classes=[AllowAny])
    def validate(self, request):
        payload = JwtToken().decode(request.GET.get('token'))
        user = self.get_queryset().filter(pk=payload['uuid'])[0]
        if not user.verified:
            self.user_service.verify_and_activate_user(user)
            return Response({}, status=status.HTTP_200_OK)
        return Response({}, status=status.HTTP_403_FORBIDDEN)
