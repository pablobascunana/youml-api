from rest_framework import viewsets, status
from rest_framework.response import Response

from api.viewsets.project.model import Project
from api.viewsets.project.serializer import ProjectSerializer
from api.viewsets.project.service import ProjectService
from users.viewsets.user.service import RegisterUserService


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    project_service = ProjectService()

    def list(self, request, *args, **kwargs):
        if request.user.role == 'ADMIN' and request.user.company:
            users = RegisterUserService().get_users_by_company_id(request.user.company_id)
            projects = self.get_queryset().filter(user__in=users.values('uuid'))
        else:
            projects = self.get_queryset().filter(user=request.user)

        json_projects = ProjectSerializer(projects, many=True).data
        return Response(json_projects, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        project = {'name': request.data['name'], 'user': request.user.uuid}
        created_project = self.project_service.create(project)
        return Response(created_project, status=status.HTTP_201_CREATED)

    def destroy(self, request, pk=None, *args, **kwargs):
        destroyed = self.project_service.delete(pk)
        return Response(status=status.HTTP_204_NO_CONTENT) if destroyed > 0 \
            else Response("Resource not found", status=status.HTTP_404_NOT_FOUND)
