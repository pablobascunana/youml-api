import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from api.viewsets import Project


@pytest.mark.django_db
class TestUserEndpoints:
    endpoint = '/api/v1/project'
    unique_fields = 'The fields user, name must make a unique set.'

    def test_list(self, client_as_admin: APIClient):
        response = client_as_admin[0].get(self.endpoint)
        assert response.status_code == 403

    def test_list_projects_without_permission(self, client: APIClient):
        response = client.get(self.endpoint)
        assert response.status_code == 403

    def test_create_project(self, client_as_user: APIClient):
        body = {"name": 'My project', "user": str(client_as_user[1].uuid)}
        response = client_as_user[0].post(f"{self.endpoint}", body, format='json')
        assert response.status_code == 201

    def test_create_project_with_existing_name(self, client_as_user: APIClient):
        baker.make(Project, name='My project', user=client_as_user[1])
        body = {"name": 'My project', "user": str(client_as_user[1].uuid)}
        response = client_as_user[0].post(f"{self.endpoint}", body, format='json')
        assert response.status_code == 400
        assert response.json()['non_field_errors'][0] == self.unique_fields

    def test_create_project_without_permissions(self, client: APIClient):
        body = {"name": 'My project', "user": 'abcd-efg'}
        response = client.post(f"{self.endpoint}", body, format='json')
        assert response.status_code == 403

    def test_update(self, client_as_admin: APIClient):
        response = client_as_admin[0].put(f"{self.endpoint}")
        assert response.status_code == 405

    def test_delete(self, client_as_admin: APIClient):
        response = client_as_admin[0].delete(f"{self.endpoint}")
        assert response.status_code == 405