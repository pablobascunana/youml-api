import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from api.viewsets.dataset.model import Dataset
from api.viewsets.project.model import Project


@pytest.mark.django_db
class TestDatasetEndpoints:
    endpoint = '/api/v1/dataset'
    unique_fields = 'The fields user, project, name must make a unique set.'

    DATASET_NAME = 'My dataset'

    def test_list_as_admin_user(self, client_as_admin: APIClient, project: Project):
        response = client_as_admin[0].get(f"{self.endpoint}?project={project.pk}")
        assert response.status_code == 200

    def test_list_as_normal_user(self, client_as_user: APIClient, project: Project):
        response = client_as_user[0].get(f"{self.endpoint}?project={project.pk}")
        assert response.status_code == 200

    def test_list_projects_without_permission(self, client: APIClient, project: Project):
        response = client.get(f"{self.endpoint}?project={project.pk}")
        assert response.status_code == 403

    def test_create_dataset(self, client_as_user: APIClient, project: Project):
        body = {"name": self.DATASET_NAME, "user": str(client_as_user[1].uuid), "project": project.pk}
        response = client_as_user[0].post(f"{self.endpoint}", body, format='json')
        assert response.status_code == 201

    def test_create_dataset_with_existing_name(self, client_as_user: APIClient, project: Project):
        baker.make(Dataset, name=self.DATASET_NAME, user=client_as_user[1], project=project)
        body = {"name": self.DATASET_NAME, "user": str(client_as_user[1].uuid), "project": project.pk}
        response = client_as_user[0].post(f"{self.endpoint}", body, format='json')
        assert response.status_code == 400
        assert response.json()['nonFieldErrors'][0] == self.unique_fields

    def test_create_dataset_without_permissions(self, client: APIClient, project: Project):
        body = {"name": self.DATASET_NAME, "user": 'abcd-efg', "project": project.pk}
        response = client.post(f"{self.endpoint}", body, format='json')
        assert response.status_code == 403

    def test_update(self, client_as_admin: APIClient):
        response = client_as_admin[0].put(f"{self.endpoint}")
        assert response.status_code == 405

    def test_delete(self, client_as_admin: APIClient, dataset: Dataset):
        response = client_as_admin[0].delete(f"{self.endpoint}/{dataset.pk}")
        assert response.status_code == 204

    def test_delete_not_existing(self, client_as_admin: APIClient):
        dataset = baker.prepare(Dataset)
        response = client_as_admin[0].delete(f"{self.endpoint}/{dataset.pk}")
        assert response.status_code == 404
