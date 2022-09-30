from rest_framework import viewsets, status
from rest_framework.response import Response

from users.models import User
from users.viewsets.user.permissions import IsAllowed
from users.viewsets.user.serializer import UserSerializer
from users.viewsets.user.service import UserService


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
        return Response({}, status=status.HTTP_201_CREATED)
