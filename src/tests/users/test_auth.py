import pytest

from rest_framework.test import APIClient

from users.models import User


@pytest.mark.django_db(transaction=True)
class TestUserEndpoints:
    endpoint = '/users/v1/auth'

    def test_list(self, client: APIClient):
        response = client.get(f"{self.endpoint}")
        assert response.status_code == 403

    def test_login(self, client_as_admin: APIClient):
        user = {'username': client_as_admin[1].username, 'password': 'fake_password'}
        response = client_as_admin[0].post(f"{self.endpoint}", user)
        assert response.status_code == 200

    def test_login_incorrect_credentials(self, client_as_admin: APIClient):
        user = {'username': client_as_admin[1].username, 'password': '1234'}
        response = client_as_admin[0].post(f"{self.endpoint}", user)
        assert response.status_code == 403

    def test_login_increase_login_attempts(self, client_as_admin: APIClient):
        user = {'username': client_as_admin[1].username, 'password': client_as_admin[1].password}
        response = client_as_admin[0].post(f"{self.endpoint}", user)
        updated_user = User.objects.filter(username=client_as_admin[1].username).first()
        assert response.status_code == 403
        assert updated_user.is_active
        assert updated_user.login_attempts == 1

    def test_login_inactive_user(self, client_as_inactive_user: APIClient):
        user = {'username': client_as_inactive_user[1].username, 'password': client_as_inactive_user[1].password}
        response = client_as_inactive_user[0].post(f"{self.endpoint}", user)
        assert response.status_code == 403
        assert not client_as_inactive_user[1].active
        assert client_as_inactive_user[1].login_attempts == 5

    def test_update(self, client_as_admin: APIClient):
        response = client_as_admin[0].put(f"{self.endpoint}")
        assert response.status_code == 405

    def test_delete(self, client_as_admin: APIClient):
        response = client_as_admin[0].delete(f"{self.endpoint}")
        assert response.status_code == 405


