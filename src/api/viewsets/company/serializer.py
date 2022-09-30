from rest_framework import serializers

from api.viewsets.company.model import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('uuid', 'name', 'cif', 'email', 'address', 'city', 'country', 'postal_code', 'sector')
