from typing import Dict

from api.viewsets import Image
from api.viewsets.image.serializer import ImageSerializer


class ImageService:

    @staticmethod
    def create(image: Dict):
        image_serializer = ImageSerializer(data=image)
        image_serializer.is_valid(raise_exception=True)
        return Image.objects.create(**image_serializer.validated_data)
