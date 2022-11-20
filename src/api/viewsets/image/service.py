from typing import Dict

from django.db.models import QuerySet

from core.utils.query import do_bulk_update
from api.viewsets import Image
from api.viewsets.image.serializer import ImageSerializer


class ImageService:

    @staticmethod
    def create(image: Dict):
        image_serializer = ImageSerializer(data=image)
        image_serializer.is_valid(raise_exception=True)
        return Image.objects.create(**image_serializer.validated_data)

    @staticmethod
    def get_mark_to_train_at_with_value_none() -> QuerySet:
        return Image.objects.filter(mark_to_train_at__isnull=True)

    def update_mark_to_train_at(self):
        images = self.get_mark_to_train_at_with_value_none()
        do_bulk_update(images, Image, ['mark_to_train_at'])

