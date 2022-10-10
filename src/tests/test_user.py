import pytest
from django.forms import model_to_dict
from model_bakery import baker
from rest_framework.test import APIClient

from users.models import User
from users.viewsets.user.service import RegisterUserService


@pytest.mark.django_db
class TestUserEndpoints:
    endpoint = '/users/v1/user'
    validate_endpoint = '/users/v1/user/validate'
    username_exists = 'user with this username already exists.'
    email_exists = 'user with this email already exists.'

    def test_list_get_users(self, client_as_admin: APIClient):
        response = client_as_admin[0].get(self.endpoint)
        assert response.status_code == 403

    def test_list_get_user_not_found(self, client_as_admin: APIClient):
        response = client_as_admin[0].get(f"{self.endpoint}/11111")
        assert response.status_code == 404

    def test_list_get_admin_user(self, client_as_admin: APIClient):
        response = client_as_admin[0].get(f"{self.endpoint}/{client_as_admin[1].pk}")
        assert response.status_code == 200
        user = response.json()
        assert user['username'] == 'user_admin'
        assert user['name'] == 'user'
        assert user['lastname'] == 'admin'
        assert user['email'] == 'admin@email.com'
        assert user['role'] == 'ADMIN'

    def test_list_get_normal_user(self, client_as_user: APIClient):
        response = client_as_user[0].get(f"{self.endpoint}/{client_as_user[1].pk}")
        assert response.status_code == 200
        user = response.json()
        assert user['username'] == 'user'
        assert user['name'] == 'user'
        assert user['lastname'] == 'user'
        assert user['email'] == 'user@email.com'
        assert user['role'] == 'NORMAL'

    def test_list_non_found(self, client_as_admin: APIClient):
        response = client_as_admin[0].get(f"{self.endpoint}/")
        assert response.status_code == 404

    def test_create_duplicate_user_and_missing_password_field(self, client_as_admin: APIClient, user: User):
        user = model_to_dict(user, fields=['username', 'name', 'lastname', 'email', 'role'])
        response = client_as_admin[0].post(f"{self.endpoint}", user)
        assert response.status_code == 400
        result = response.json()
        assert result['username'][0] == self.username_exists
        assert result['email'][0] == self.email_exists
        assert result['password'][0] == 'This field is required.'

    def test_create_duplicate_username(self, client_as_admin: APIClient, user: User):
        user = model_to_dict(user, fields=['username', 'name', 'lastname', 'email', 'role'])
        response = client_as_admin[0].post(f"{self.endpoint}", user)
        assert response.status_code == 400
        assert response.json()['username'][0] == self.username_exists

    def test_create_duplicate_email(self, client_as_admin: APIClient, user: User):
        user = model_to_dict(user, fields=['username', 'name', 'lastname', 'email', 'role'])
        response = client_as_admin[0].post(f"{self.endpoint}", user)
        assert response.status_code == 400
        assert response.json()['email'][0] == self.email_exists

    def test_create(self, client_as_admin: APIClient):
        user = {"username": "username", "name": "name", "lastname": "lastname", "email": "user_email@email.com",
                "password": "user_password", "role": "ADMIN"}
        response = client_as_admin[0].post(f"{self.endpoint}", user)
        assert response.status_code == 202

    def test_update(self, client_as_admin: APIClient):
        response = client_as_admin[0].put(f"{self.endpoint}")
        assert response.status_code == 405

    def test_delete(self, client_as_admin: APIClient):
        response = client_as_admin[0].delete(f"{self.endpoint}")
        assert response.status_code == 405

    def test_validate(self, client_as_user: APIClient):
        user = baker.make(User)
        token = RegisterUserService().create_validation_token(user)
        response = client_as_user[0].get(f"{self.validate_endpoint}?token={token}&uuid={str(user.uuid)}")
        assert response.status_code == 200

    def test_validate_forbidden(self, client_as_user: APIClient):
        user = baker.make(User, active=True, verified=True)
        token = RegisterUserService().create_validation_token(user)
        response = client_as_user[0].get(f"{self.validate_endpoint}?token={token}&uuid={str(user.uuid)}")
        assert response.status_code == 403
