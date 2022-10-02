from django.http import QueryDict

from api.viewsets.company.serializer import CompanySerializer


class CompanyService:

    @staticmethod
    def create_company(company: QueryDict):
        company_serializer = CompanySerializer(data=company)
        company_serializer.is_valid(raise_exception=True)
        company_serializer.save()

