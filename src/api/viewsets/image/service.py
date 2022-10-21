from typing import Dict

from api.viewsets.image.serializer import ImageSerializer


class ImageService:

    @staticmethod
    def create(image: Dict):
        image_serializer = ImageSerializer(data=image)
        image_serializer.is_valid(raise_exception=True)
        image_serializer.save()
