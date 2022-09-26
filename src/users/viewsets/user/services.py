from django.contrib.auth import get_user_model
from django.http import QueryDict

from users.viewsets.user.serializer import UserSerializer


class UserService:

    @staticmethod
    def create_user(user: QueryDict):
        user_serializer = UserSerializer(data=user)
        user_serializer.is_valid(raise_exception=True)
        get_user_model().objects.create_user(name=user['name'], lastname=user['lastname'], email=user['email'],
                                             username=user['username'], password=user['password'])
