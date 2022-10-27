from rest_framework import serializers

from api.viewsets.image.model import Image


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('uuid', 'name', 'dataset')
        extra_kwargs = {
            'dataset': {'write_only': True}
        }
