import pytest
from django.forms import model_to_dict
from rest_framework.test import APIClient

from api.viewsets.company.model import Company
from users.models import User


@pytest.mark.django_db(transaction=True)
class TestUserEndpoints:
    endpoint = '/api/v1/company'
    cif_exists = 'company with this cif already exists.'
    company_email_exists = 'company with this email already exists.'
    username_exists = 'user with this username already exists.'
    username_email_exists = 'user with this email already exists.'

    def test_list_get_companies_with_permission(self, client_as_admin: APIClient):
        response = client_as_admin[0].get(self.endpoint)
        assert response.status_code == 403

    def test_list_get_companies_not_found(self, client_as_admin: APIClient):
        response = client_as_admin[0].get(f"{self.endpoint}/11111")
        assert response.status_code == 404

    def test_list_get_companies_without_permission(self, client: APIClient):
        response = client.get(self.endpoint)
        assert response.status_code == 403

    def test_list_get_company_without_permission(self, client: APIClient):
        response = client.get(f"{self.endpoint}/11111")
        assert response.status_code == 403

    def test_list_create_company_and_user(self, client: APIClient):
        company = {"name": "company_name", "email": "company_email@email.com", "cif": "C12571322"}
        user = {"username": "username", "name": "name", "lastname": "lastname", "email": "user_email@email.com",
                "password": "user_password", "role": "ADMIN"}
        body = {"company": company, "user": user}
        response = client.post(f"{self.endpoint}", body, format='json')
        assert response.status_code == 202

    def test_list_create_company_and_user_with_existing_company_unique_fields(self, client: APIClient, company: Company,
                                                                              company_user: User):
        body = {"company": model_to_dict(company, fields=['name', 'email', 'cif']),
                "user": model_to_dict(company_user,
                                      fields=['username', 'name', 'lastname', 'email', 'password', 'role'])}
        response = client.post(f"{self.endpoint}", body, format='json')
        assert response.status_code == 400
        result = response.json()
        assert result['email'][0] == self.company_email_exists
        assert result['cif'][0] == self.cif_exists

    def test_list_create_company_and_user_with_existing_user_unique_fields(self, client: APIClient, company_user: User):
        company = {"name": "company_name", "email": "company_email@email.com", "cif": "C12571322"}
        body = {"company": company, "user": model_to_dict(
            company_user, fields=['username', 'name', 'lastname', 'email', 'password', 'role'])}
        response = client.post(f"{self.endpoint}", body, format='json')
        assert response.status_code == 400
        result = response.json()
        assert result['email'][0] == self.username_email_exists
        assert result['username'][0] == self.username_exists

    def test_update(self, client_as_admin: APIClient):
        response = client_as_admin[0].put(f"{self.endpoint}")
        assert response.status_code == 405

    def test_delete(self, client_as_admin: APIClient):
        response = client_as_admin[0].delete(f"{self.endpoint}")
        assert response.status_code == 405
