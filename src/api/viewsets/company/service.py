from typing import Dict

from django.http import QueryDict

from api.viewsets.company.model import Company
from api.viewsets.company.serializer import CompanySerializer


class CompanyService:

    @staticmethod
    def create_company(company: QueryDict) -> Dict:
        company_serializer = CompanySerializer(data=company)
        company_serializer.is_valid(raise_exception=True)
        company_serializer.save()
        return company_serializer.data

