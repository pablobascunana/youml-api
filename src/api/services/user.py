from django.contrib.auth import get_user_model

from users.models import User


class UserService:

    @staticmethod
    def create_user(user: User):
        get_user_model().objects.create_user(name=user['name'], lastname=user['lastname'], email=user['email'],
                                             username=user['username'], password=user['password'])
