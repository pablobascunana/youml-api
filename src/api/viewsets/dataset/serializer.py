from rest_framework import serializers

from api.viewsets.dataset.model import Dataset


class DatasetSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    @staticmethod
    def get_created_at(obj):
        return obj.created_at.strftime("%d-%m-%Y %H:%M:%S")

    class Meta:
        model = Dataset
        fields = '__all__'
