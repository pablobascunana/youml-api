from rest_framework import viewsets, status
from rest_framework.response import Response

from api.viewsets.project.model import Project
from api.viewsets.project.serializer import ProjectSerializer
from api.viewsets.project.service import ProjectService


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @staticmethod
    def list(request, *args, **kwargs):
        # TODO FUTURE, for now it is not possible get projects
        return Response(status=status.HTTP_403_FORBIDDEN)

    @staticmethod
    def create(request, *args, **kwargs):
        project = {'name': request.data['name'], 'user': request.user.uuid}
        created_project = ProjectService().create_project(project)
        return Response(created_project, status=status.HTTP_201_CREATED)