from rest_framework import serializers

from api.viewsets.dataset.model import Dataset
from core.utils.date import datetime_date_to_str


class DatasetSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    @staticmethod
    def get_created_at(obj):
        return datetime_date_to_str(obj.created_at)

    class Meta:
        model = Dataset
        fields = '__all__'
