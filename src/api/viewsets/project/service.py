import os
from typing import Dict

from api.viewsets.project.model import Project
from api.viewsets.project.serializer import ProjectSerializer


class ProjectService:

    @staticmethod
    def create(project: Dict) -> Dict:
        project_serializer = ProjectSerializer(data=project)
        project_serializer.is_valid(raise_exception=True)
        project_serializer.save()
        return project_serializer.data

    @staticmethod
    def get_by_id(project_id: int) -> Project:
        return Project.objects.get(pk=project_id)

    @staticmethod
    def delete(project_uuid: str):
        return Project.objects.filter(pk=project_uuid).delete()[0]

    @staticmethod
    def get_storage(storage_name: str) -> str:
        if os.getenv('STORAGE_TYPE') == 'LOCAL':
            return f"{os.getenv('STORAGE_PATH')}/{storage_name}"
        return storage_name
