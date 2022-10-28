import pytest

from rest_framework.test import APIClient

from users.models import User


@pytest.mark.django_db(transaction=True)
class TestAuthEndpoints:
    endpoint = '/users/v1/auth'
    endpoint_logout = '/users/v1/auth/logout'

    def test_list(self, client: APIClient):
        response = client.get(self.endpoint)
        assert response.status_code == 403

    def test_login(self, client_as_admin: APIClient):
        user = {'username': client_as_admin[1].username, 'password': 'fake_password'}
        response = client_as_admin[0].post(self.endpoint, user)
        assert response.status_code == 200

    def test_login_incorrect_credentials(self, client_as_admin: APIClient):
        user = {'username': client_as_admin[1].username, 'password': 'fake_password_2'}
        response = client_as_admin[0].post(self.endpoint, user)
        assert response.status_code == 403

    def test_login_increase_login_attempts(self, client_as_admin: APIClient):
        user = {'username': client_as_admin[1].username, 'password': client_as_admin[1].password}
        response = client_as_admin[0].post(self.endpoint, user)
        updated_user = User.objects.filter(username=client_as_admin[1].username).first()
        assert response.status_code == 403
        assert updated_user.is_active
        assert updated_user.login_attempts == 1

    def test_login_inactive_user(self, client_as_inactive_user: APIClient):
        user = {'username': client_as_inactive_user[1].username, 'password': client_as_inactive_user[1].password}
        response = client_as_inactive_user[0].post(self.endpoint, user)
        assert response.status_code == 403
        assert not client_as_inactive_user[1].active
        assert client_as_inactive_user[1].login_attempts == 5

    def test_update(self, client_as_admin: APIClient):
        response = client_as_admin[0].put(self.endpoint)
        assert response.status_code == 405

    def test_delete(self, client_as_admin: APIClient):
        response = client_as_admin[0].delete(self.endpoint)
        assert response.status_code == 405

    def test_list_logout(self, client_as_admin: APIClient):
        response = client_as_admin[0].get(self.endpoint_logout)
        assert response.status_code == 405

    def test_list_logout_without_login(self, client: APIClient):
        response = client.get(self.endpoint_logout)
        assert response.status_code == 403

    def test_logout_as_adming(self, client_as_admin: APIClient):
        response = client_as_admin[0].post(self.endpoint_logout, {})
        assert response.status_code == 200

    def test_logout_as_user(self, client_as_user: APIClient):
        response = client_as_user[0].post(self.endpoint_logout, {})
        assert response.status_code == 200

    def test_logout_without_login(self, client: APIClient):
        response = client.post(self.endpoint_logout, {})
        assert response.status_code == 403
