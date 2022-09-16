from rest_framework import viewsets, status
from rest_framework.response import Response

from users.models import User
from users.viewsets.user.serializer import UserSerializer
from users.viewsets.user.services import UserService


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @staticmethod
    def list(request, *args, **kwargs):
        return Response(status=status.HTTP_403_FORBIDDEN)

    @staticmethod
    def create(request, *args, **kwargs):
        UserService.create_user(request.data)
        return Response({}, status=status.HTTP_201_CREATED)
