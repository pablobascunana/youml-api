import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
class TestUserEndpoints:
    endpoint = '/users/v1/user'
    user = {
        "uuid": "39cb5f20-4154-4cb1-be51-827fe3303ce9",
        "username": "user_admin",
        "name": "user",
        "lastname": "admin",
        "email": "admin@email.com",
        "role": "ADMIN"
    }
    new_user = {
        "username": "new_user",
        "name": "new",
        "lastname": "user",
        "email": "new_user@email.com",
        "password": "1234",
        "role": "ADMIN"
    }
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

    def test_create_duplicate_user_and_missing_password_field(self, client_as_admin: APIClient):
        response = client_as_admin[0].post(f"{self.endpoint}", self.user)
        assert response.status_code == 400
        result = response.json()
        assert result['username'][0] == self.username_exists
        assert result['email'][0] == self.email_exists
        assert result['password'][0] == 'This field is required.'

    def test_create_duplicate_username(self, client_as_admin: APIClient):
        self.user['password'] = '1234'
        self.user['email'] = 'admin2@email.com'
        response = client_as_admin[0].post(f"{self.endpoint}", self.user)
        assert response.status_code == 400
        assert response.json()['username'][0] == self.username_exists

    def test_create_duplicate_email(self, client_as_admin: APIClient):
        self.user['password'] = '1234'
        self.user['username'] = 'admin2'
        self.user['email'] = 'admin@email.com'
        response = client_as_admin[0].post(f"{self.endpoint}", self.user)
        assert response.status_code == 400
        assert response.json()['email'][0] == self.email_exists

    def test_create(self, client_as_admin: APIClient):
        response = client_as_admin[0].post(f"{self.endpoint}", self.new_user)
        assert response.status_code == 201

    def test_update(self, client_as_admin: APIClient):
        response = client_as_admin[0].put(f"{self.endpoint}")
        assert response.status_code == 405

    def test_delete(self, client_as_admin: APIClient):
        response = client_as_admin[0].delete(f"{self.endpoint}")
        assert response.status_code == 405

    # def test_list_without_permission(self, client: APIClient):
    #     response = client.get(self.endpoint)
    #     assert response == 403
    #
    # def test_list_non_existing(self):
    #     pass
    #
    # def test_retrieve(self):
    #     pass
    #
    # def test_update(self):
    #     pass
    #
    # def test_delete(self):
    #     pass
    #
