from rest_framework import serializers

from api.viewsets.project.model import Project


class ProjectSerializer(serializers.ModelSerializer):

    def to_representation(self, value):
        return {
            "uuid": value.uuid,
            "name": value.name,
            "creationDate": value.creation_date.strftime("%d-%m-%Y %H:%M:%S"),
            "user": value.user.uuid
        }

    class Meta:
        model = Project
        fields = '__all__'
