from typing import Tuple

import pytest
from rest_framework.test import APIClient

from api.viewsets import Dataset
from api.viewsets.project.model import Project
from users.models import User


@pytest.mark.django_db
class TestProjectEndpoints:
    endpoint = '/api/v1/train'
    mark_to_train_endpoint = '/api/v1/train/mark-to-train'

    def test_list_trainings_as_admin_user(self, client_as_admin: APIClient):
        response = client_as_admin[0].get(self.endpoint)
        assert response.status_code == 405

    def test_list_trainings_as_normal_user(self, client_as_user: APIClient):
        response = client_as_user[0].get(self.endpoint)
        assert response.status_code == 405

    def test_list_trainings_without_permission(self, client: APIClient):
        response = client.get(self.endpoint)
        assert response.status_code == 403

    def test_retrieve_trainings_as_admin_user(self, dataset_to_train_with_admin_user: Tuple[APIClient, User]):
        dataset = dataset_to_train_with_admin_user[1]
        response = dataset_to_train_with_admin_user[0][0].get(f'{self.endpoint}/{dataset.pk}')
        assert response.status_code == 200

    def test_retrieve_trainings_as_normal_user(self, dataset_to_train_with_normal_user: Tuple[APIClient, User]):
        dataset = dataset_to_train_with_normal_user[1]
        response = dataset_to_train_with_normal_user[0][0].get(f'{self.endpoint}/{dataset.pk}')
        assert response.status_code == 200

    def test_retrieve_trainings_without_permission(self, client: APIClient, dataset_to_train: Dataset):
        response = client.get(f'{self.endpoint}/{dataset_to_train.pk}')
        assert response.status_code == 403

    def test_mark_to_train(self, client_as_user: APIClient, dataset_to_train: Dataset):
        response = client_as_user[0].post(f"{self.mark_to_train_endpoint}", {"dataset": dataset_to_train.uuid},
                                          format='json')
        assert response.status_code == 200

    def test_mark_to_train_without_permissions(self, client: APIClient, dataset_to_train: Dataset):
        response = client.post(f"{self.mark_to_train_endpoint}", {"dataset": dataset_to_train.uuid}, format='json')
        assert response.status_code == 403

    def test_update(self, client_as_admin: APIClient):
        response = client_as_admin[0].put(f"{self.endpoint}")
        assert response.status_code == 405

    def test_delete(self, client_as_admin: APIClient, project: Project):
        response = client_as_admin[0].delete(f"{self.endpoint}")
        assert response.status_code == 405
