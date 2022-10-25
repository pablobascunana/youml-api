from rest_framework import viewsets, status
from rest_framework.response import Response

from api.viewsets import ImageLabels
from api.viewsets.label.model import Label
from api.viewsets.label.serializer import LabelSerializer


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    @staticmethod
    def update(request, pk=None, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None, *args, **kwargs):
        label = ImageLabels.objects.filter(label=pk)
        if label.exists():
            self.get_queryset().filter(pk=pk).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
