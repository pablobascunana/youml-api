import logging

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.http import QueryDict

from core.utils.file import read_file
from users.models import User
from users.viewsets.user.serializer import UserSerializer


class RegisterUserService:

    def create_user(self, user: QueryDict):
        user_serializer = UserSerializer(data=user)
        user_serializer.is_valid(raise_exception=True)
        created_user = get_user_model().objects.create_user(name=user['name'], lastname=user['lastname'],
                                                            email=user['email'], username=user['username'],
                                                            password=user['password'], role=user['role'])
        logging.info(f"UserService: The user with this email {user['email']} has been created successfully")
        return self.create_validation_token(created_user)

    @staticmethod
    def create_validation_token(user: User) -> str:
        return default_token_generator.make_token(user)

    @staticmethod
    def check_validation_token(user: User, token: str) -> bool:
        return default_token_generator.check_token(user, token)
