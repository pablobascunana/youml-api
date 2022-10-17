from typing import Dict

from api.viewsets import Project
from api.viewsets.project.serializer import ProjectSerializer


class ProjectService:

    @staticmethod
    def create(project: Dict) -> Dict:
        project_serializer = ProjectSerializer(data=project)
        project_serializer.is_valid(raise_exception=True)
        project_serializer.save()
        return project_serializer.data

    @staticmethod
    def delete(project_uuid: str):
        return Project.objects.filter(pk=project_uuid).delete()[0]
