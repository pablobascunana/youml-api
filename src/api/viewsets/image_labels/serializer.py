from rest_framework import serializers

from api.viewsets.image_labels.model import ImageLabels


class ImageLabelSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImageLabels
        fields = '__all__'
