import pytest
from django.test.client import MULTIPART_CONTENT, encode_multipart, BOUNDARY
from django.core.files.base import ContentFile
from model_bakery import baker
from rest_framework.test import APIClient

from api.viewsets import Dataset, Image
from api.viewsets.project.model import Project


@pytest.mark.django_db
class TestProjectEndpoints:
    endpoint = '/api/v1/image'
    unique_fields = 'The fields dataset, name must make a unique set.'

    IMAGE_NAME = "image.png"

    def test_list_as_admin_user(self, client_as_admin: APIClient):
        response = client_as_admin[0].get(self.endpoint)
        assert response.status_code == 405

    def test_list_as_normal_user(self, client_as_user: APIClient):
        response = client_as_user[0].get(self.endpoint)
        assert response.status_code == 405

    def test_list_projects_without_permission(self, client: APIClient):
        response = client.get(self.endpoint)
        assert response.status_code == 403

    def test_create_image(self, client_as_user: APIClient, project: Project, dataset: Dataset):
        document = ContentFile(b"some_data", self.IMAGE_NAME)
        response = client_as_user[0].post(self.endpoint, data=encode_multipart(
            data=dict(file=document, filename=self.IMAGE_NAME, dataset=dataset.uuid, project=project.uuid),
            boundary=BOUNDARY), content_type=MULTIPART_CONTENT)
        assert response.status_code == 201

    def test_create_image_with_existing_name(self, client_as_user: APIClient, project: Project, dataset: Dataset):
        image = baker.make(Image, name=self.IMAGE_NAME, dataset=dataset)
        document = ContentFile(b"some_data", image.name)
        response = client_as_user[0].post(self.endpoint, data=encode_multipart(
            data=dict(file=document, filename=image.name, dataset=dataset.uuid, project=project.uuid),
            boundary=BOUNDARY), content_type=MULTIPART_CONTENT)
        assert response.status_code == 400
        assert response.json()['non_field_errors'][0] == self.unique_fields

    def test_create_image_without_permissions(self, client: APIClient, project: Project, dataset: Dataset):
        document = ContentFile(b"some_data", self.IMAGE_NAME)
        response = client.post(self.endpoint, data=encode_multipart(
            data=dict(file=document, filename=self.IMAGE_NAME, dataset=dataset.uuid, project=project.uuid),
            boundary=BOUNDARY), content_type=MULTIPART_CONTENT)
        assert response.status_code == 403

    def test_update_not_found(self, client_as_admin: APIClient, image: Image):
        response = client_as_admin[0].put(f"{self.endpoint}/{image.pk}")
        assert response.status_code == 404

    def test_update_not_allow(self, client_as_admin: APIClient):
        response = client_as_admin[0].put(f"{self.endpoint}")
        assert response.status_code == 405

    def test_delete_not_found(self, client_as_admin: APIClient, image: Image):
        response = client_as_admin[0].delete(f"{self.endpoint}/{image.pk}")
        assert response.status_code == 404

    def test_delete_not_allow(self, client_as_admin: APIClient):
        response = client_as_admin[0].delete(f"{self.endpoint}")
        assert response.status_code == 405
