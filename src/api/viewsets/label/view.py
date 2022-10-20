from rest_framework import viewsets

from api.viewsets.label.model import Label
from api.viewsets.label.serializer import LabelSerializer


class LabelViewSet(viewsets.ModelViewSet):
    queryset = Label.objects.all()
    serializer_class = LabelSerializer

