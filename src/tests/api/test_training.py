import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from api.viewsets import Dataset, Training
from api.viewsets.project.model import Project


@pytest.mark.django_db
class TestProjectEndpoints:
    endpoint = '/api/v1/mark-to-train'

    def test_list_as_admin_user(self, client_as_admin: APIClient):
        response = client_as_admin[0].get(self.endpoint)
        assert response.status_code == 405

    def test_list_as_normal_user(self, client_as_user: APIClient):
        response = client_as_user[0].get(self.endpoint)
        assert response.status_code == 405

    def test_list_projects_without_permission(self, client: APIClient):
        response = client.get(self.endpoint)
        assert response.status_code == 403

    def test_create_training(self, client_as_user: APIClient, dataset_to_train: Dataset):
        response = client_as_user[0].post(f"{self.endpoint}", {"dataset": dataset_to_train.uuid}, format='json')
        assert response.status_code == 200

    def test_create_training_without_permissions(self, client: APIClient, dataset_to_train: Dataset):
        response = client.post(f"{self.endpoint}", {"dataset": dataset_to_train.uuid}, format='json')
        assert response.status_code == 403

    def test_update(self, client_as_admin: APIClient):
        response = client_as_admin[0].put(f"{self.endpoint}")
        assert response.status_code == 405

    def test_delete(self, client_as_admin: APIClient, project: Project):
        response = client_as_admin[0].delete(f"{self.endpoint}")
        assert response.status_code == 405
