from typing import List

from django.db.models import QuerySet
from django.db.models.base import ModelBase

from core.utils.date import date_now


def do_bulk_update(query_set: QuerySet, entity: ModelBase, fields_to_update: List):
    to_update = []
    for image in list(query_set):
        image.mark_to_train_at = date_now()
        to_update.append(image)
        if len(to_update) == 1000:
            entity.objects.bulk_update(to_update)
            to_update = []
    entity.objects.bulk_update(to_update, fields_to_update)
