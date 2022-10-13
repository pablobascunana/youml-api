import datetime
import logging
import os

import jwt
from typing import Dict, Union

from django.contrib.auth import get_user_model
from django.http import QueryDict
from jwt import DecodeError, ExpiredSignatureError

from users.models import User
from users.viewsets.user.serializer import UserSerializer


class RegisterUserService:

    def create_user(self, user: QueryDict) -> str:
        self.validate_user(user)
        created_user = get_user_model().objects.create_user(name=user['name'], lastname=user['lastname'],
                                                            email=user['email'], username=user['username'],
                                                            password=user['password'], role=user['role'])
        logging.info(f"UserService: The user with this email {user['email']} has been created successfully")
        return self.create_validation_jwt(created_user)

    def create_company_user(self, user: QueryDict) -> str:
        self.validate_user(user)
        created_user = get_user_model().objects.create_company_user(name=user['name'], lastname=user['lastname'],
                                                                    email=user['email'], username=user['username'],
                                                                    password=user['password'], role=user['role'],
                                                                    company=user['company'])
        logging.info(f"UserService: The user with this email {user['email']} and belong to this company id "
                     f"{user['company'].uuid} has been created successfully")
        return self.create_validation_jwt(created_user)

    @staticmethod
    def validate_user(user: QueryDict):
        user_serializer = UserSerializer(data=user)
        user_serializer.is_valid(raise_exception=True)

    def verify_and_activate_user(self, user: User):
        user.verified = True
        user.active = True
        self.save_user(user)

    def activate_or_deactivate_user(self, user: User, active: bool):
        user.active = active
        self.save_user(user)

    def update_login_attempts(self, user: User, attempts: int):
        user.login_attempts = attempts
        self.save_user(user)

    @staticmethod
    def save_user(user: User):
        user.save()

    @staticmethod
    def create_validation_jwt(user: User) -> str:
        exp_timestamp = datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=1)
        return jwt.encode({'exp': exp_timestamp, 'uuid': str(user.uuid)}, os.getenv('JWT_USER_VALIDATION'),
                          algorithm="HS256")

    @staticmethod
    def check_validation_jwt(token: str) -> Union[Dict, bool]:
        try:
            return jwt.decode(token, os.getenv('JWT_USER_VALIDATION'), algorithms=["HS256"])
        except (DecodeError, ExpiredSignatureError):
            return False
