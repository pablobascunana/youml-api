from rest_framework import serializers

from api.viewsets.project.model import Project


class ProjectSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()

    @staticmethod
    def get_created_at(obj):
        return obj.created_at.strftime("%d-%m-%Y %H:%M:%S")

    class Meta:
        model = Project
        fields = '__all__'
        extra_kwargs = {
            'storage_in': {'write_only': True}
        }
