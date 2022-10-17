from rest_framework import serializers

from api.viewsets.dataset.model import Dataset


class DatasetSerializer(serializers.ModelSerializer):

    @classmethod
    def to_representation(cls, value):
        return {
            "uuid": value.uuid,
            "name": value.name,
            "createdAt": value.created_at.strftime("%d-%m-%Y %H:%M:%S"),
            "user": value.user_id,
            "project": value.project_id
        }

    class Meta:
        model = Dataset
        fields = '__all__'
