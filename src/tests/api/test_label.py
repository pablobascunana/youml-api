import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from api.viewsets import ImageLabels, Image
from api.viewsets.dataset.model import Dataset
from api.viewsets.label.model import Label


@pytest.mark.django_db
class TestLabelEndpoints:
    endpoint = '/api/v1/label'
    unique_fields = 'The fields dataset, name must make a unique set.'

    LABEL_NAME = 'My label'

    def test_list_as_admin_user(self, client_as_admin: APIClient):
        response = client_as_admin[0].get(self.endpoint)
        assert response.status_code == 200

    def test_list_as_normal_user(self, client_as_user: APIClient):
        response = client_as_user[0].get(self.endpoint)
        assert response.status_code == 200

    def test_list_projects_without_permission(self, client: APIClient):
        response = client.get(self.endpoint)
        assert response.status_code == 403

    def test_create(self, client_as_user: APIClient, dataset: Dataset):
        body = {"name": self.LABEL_NAME, "dataset": dataset.pk}
        response = client_as_user[0].post(f"{self.endpoint}", body, format='json')
        assert response.status_code == 201

    def test_create_with_existing_name(self, client_as_user: APIClient, dataset: Dataset):
        baker.make(Label, name=self.LABEL_NAME, dataset=dataset)
        body = {"name": self.LABEL_NAME, "dataset": dataset.pk}
        response = client_as_user[0].post(f"{self.endpoint}", body, format='json')
        assert response.status_code == 400
        assert response.json()['nonFieldErrors'][0] == self.unique_fields

    def test_create_without_permissions(self, client: APIClient):
        body = {"name": self.LABEL_NAME, "user": 'abcd-efg'}
        response = client.post(f"{self.endpoint}", body, format='json')
        assert response.status_code == 403

    def test_update(self, client_as_admin: APIClient, label: Label):
        response = client_as_admin[0].put(f"{self.endpoint}/{label.pk}")
        assert response.status_code == 405

    def test_delete(self, client_as_admin: APIClient, label: Label):
        response = client_as_admin[0].delete(f"{self.endpoint}/{label.pk}")
        assert response.status_code == 204

    def test_delete_existing(self, client_as_admin: APIClient, image: Image, label: Label):
        baker.make(ImageLabels, label=label, image=image)
        response = client_as_admin[0].delete(f"{self.endpoint}/{label.pk}")
        assert response.status_code == 400

    def test_delete_not_found(self, client_as_admin: APIClient):
        response = client_as_admin[0].delete(f"{self.endpoint}/60a7f3a2-122c-450b-aaa6-703eb4bbe540")
        assert response.status_code == 404
