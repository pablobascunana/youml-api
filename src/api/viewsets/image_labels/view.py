from rest_framework import viewsets, status
from rest_framework.response import Response

from api.viewsets.image_labels.model import ImageLabels
from api.viewsets.image_labels.serializer import ImageLabelSerializer


class ImageLabelViewSet(viewsets.ModelViewSet):
    queryset = ImageLabels.objects.all()
    serializer_class = ImageLabelSerializer

    @staticmethod
    def list(request, pk=None, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @staticmethod
    def update(request, pk=None, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @staticmethod
    def destroy(request, pk=None, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
