from rest_framework import viewsets, status
from rest_framework.response import Response

from api.viewsets.label.model import Label
from api.viewsets.label.serializer import LabelSerializer


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    @staticmethod
    def list(request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @staticmethod
    def update(request, pk=None, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    @staticmethod
    def destroy(request, pk=None, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
