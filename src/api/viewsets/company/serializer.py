from rest_framework import serializers

from api.viewsets.company.model import Company


class CompanySerializer(serializers.ModelSerializer):
    postalCode = serializers.IntegerField(source="postal_code", required=False)

    class Meta:
        model = Company
        fields = ('uuid', 'name', 'cif', 'email', 'address', 'city', 'country', 'postalCode', 'sector')
