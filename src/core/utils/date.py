from datetime import datetime

from django.utils import timezone


def date_now():
    return datetime.now(tz=timezone.utc)


def datetime_date_to_str(date: datetime) -> str:
    return date.strftime("%d-%m-%Y %H:%M:%S")


def str_date_to_db_datetime(date: str) -> str:
    return datetime.strptime(date, "%d-%m-%Y %H:%M:%S").strftime("%Y-%m-%d %H:%M:%S")
