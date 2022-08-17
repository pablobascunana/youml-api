from rest_framework import viewsets, status
from rest_framework.response import Response

from users.models import User
from users.viewsets.user.serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    # filterset_class = UserFilter
    serializer_class = UserSerializer

    def list(self, request):
        return Response(status=status.HTTP_403_FORBIDDEN)
