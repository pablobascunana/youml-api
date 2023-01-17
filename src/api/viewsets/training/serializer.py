from rest_framework import serializers

from api.viewsets.training.model import Training
from core.utils.date import datetime_date_to_str


class TrainingSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    username = serializers.SerializerMethodField()
    project_name = serializers.SerializerMethodField()
    dataset_name = serializers.SerializerMethodField()

    @staticmethod
    def get_created_at(obj):
        return datetime_date_to_str(obj.created_at)

    @staticmethod
    def get_username(obj):
        return obj.user.username

    @staticmethod
    def get_project_name(obj):
        return obj.dataset.project.name

    @staticmethod
    def get_dataset_name(obj):
        return obj.dataset.name

    class Meta:
        model = Training
        fields = '__all__'
        extra_kwargs = {
            'dataset': {'write_only': True},
            'user': {'write_only': True}
        }
