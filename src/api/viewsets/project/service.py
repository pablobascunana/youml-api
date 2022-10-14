from typing import Dict

from api.viewsets.project.serializer import ProjectSerializer


class ProjectService:

    @staticmethod
    def create_project(project: Dict) -> Dict:
        project_serializer = ProjectSerializer(data=project)
        project_serializer.is_valid(raise_exception=True)
        project_serializer.save()
        return project_serializer.data
