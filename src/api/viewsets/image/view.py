import os

from rest_framework import viewsets, status
from rest_framework.response import Response

from api.viewsets.image.model import Image
from api.viewsets.image.service import ImageService
from api.viewsets.project.service import ProjectService
from core.providers.file_system import FileManagerProvider


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()

    @staticmethod
    def list(request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @staticmethod
    def create(request, *args, **kwargs):
        project = ProjectService().get_by_id(request.data['project'])
        file_system = FileManagerProvider(os.getenv('STORAGE_TYPE')).provider
        filename = file_system.format_filename(request.data['filename'])
        filepath = file_system.create_path(project.storage_in, request.data['dataset'])
        file_system.create_directory(filepath)
        file_system.save_file(f'{filepath}/{filename}', request.data['file'].read())
        image = {"name": filename, "dataset": request.data['dataset']}
        ImageService().create(image)
        return Response(status=status.HTTP_201_CREATED)
