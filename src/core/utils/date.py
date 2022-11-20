from datetime import datetime

from django.utils import timezone


def date_now():
    return datetime.now(tz=timezone.utc)
