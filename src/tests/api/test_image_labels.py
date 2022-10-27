import pytest
from rest_framework.test import APIClient

from api.viewsets import Image
from api.viewsets.label.model import Label


@pytest.mark.django_db
class TestLabelEndpoints:
    endpoint = '/api/v1/image-label'

    def test_list(self, client_as_admin: APIClient):
        response = client_as_admin[0].get(self.endpoint)
        assert response.status_code == 405

    def test_create(self, client_as_admin: APIClient, image: Image, label: Label):
        body = {"image": image.pk, "label": label.pk}
        response = client_as_admin[0].post(f"{self.endpoint}", body, format='json')
        assert response.status_code == 201

    def test_create_without_permissions(self, client: APIClient, image: Image, label: Label):
        body = {"image": image.pk, "label": label.pk}
        response = client.post(f"{self.endpoint}", body, format='json')
        assert response.status_code == 403

    def test_update(self, client_as_admin: APIClient, label: Label):
        response = client_as_admin[0].put(f"{self.endpoint}/{label.pk}")
        assert response.status_code == 405

    def test_destroy(self, client_as_admin: APIClient, label: Label):
        response = client_as_admin[0].delete(f"{self.endpoint}/{label.pk}")
        assert response.status_code == 405
