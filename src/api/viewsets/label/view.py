from rest_framework import viewsets, status
from rest_framework.response import Response

from api.viewsets.image_labels.service import ImageLabelService
from api.viewsets.label.model import Label
from api.viewsets.label.serializer import LabelSerializer


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

    @staticmethod
    def update(request, pk=None, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None, *args, **kwargs):
        label = ImageLabelService().filter_by_label_id(pk)
        if label.exists():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        destroyed = self.get_queryset().filter(pk=pk).delete()[0]
        return Response(status=status.HTTP_204_NO_CONTENT) if destroyed > 0 \
            else Response("Resource not found", status=status.HTTP_404_NOT_FOUND)
