from rest_framework import serializers

from api.viewsets.project.model import Project


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'
