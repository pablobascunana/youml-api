from rest_framework import serializers

from api.viewsets.project.model import Project
from core.utils.date import datetime_date_to_str


class ProjectSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    @staticmethod
    def get_created_at(obj):
        return datetime_date_to_str(obj.created_at)

    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {
            'storage_in': {'write_only': True}
        }
