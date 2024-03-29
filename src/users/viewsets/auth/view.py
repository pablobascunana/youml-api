from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets, status, mixins
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.utils.date import date_now
from users.models import User
from core.permissions import IsAllowed
from users.viewsets.user.serializer import UserSerializer
from users.viewsets.user.service import RegisterUserService


ATTEMPTS = 5


class AuthViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAllowed]

    user_service = RegisterUserService()

    def create(self, request, *args, **kwargs):
        if user := authenticate(username=request.data['username'], password=request.data['password']):
            if user.active:
                login(request, user)
                user.last_login = date_now()
                self.user_service.update_login_attempts(user, 0)
                return Response(status=status.HTTP_200_OK)

        user = self.get_queryset().filter(username=request.data['username']).first()
        if user and user.login_attempts < ATTEMPTS:
            attempts = user.login_attempts + 1
            self.user_service.update_login_attempts(user, attempts)
        if user and user.login_attempts == ATTEMPTS:
            self.user_service.activate_or_deactivate_user(user, False)

        return Response(status=status.HTTP_403_FORBIDDEN)

    @action(methods=["post"], name="logout", url_path='logout', url_name="Logout user", detail=False,
            permission_classes=[IsAuthenticated])
    def logout(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)
