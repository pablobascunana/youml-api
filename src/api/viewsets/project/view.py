from rest_framework import viewsets, status
from rest_framework.response import Response

from api.viewsets.project.model import Project
from api.viewsets.project.serializer import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @staticmethod
    def create(request, *args, **kwargs):
        name = request.data['name']
        return Response({}, status=status.HTTP_201_CREATED)
