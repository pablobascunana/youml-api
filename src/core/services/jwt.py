import contextlib
from typing import Dict

import jwt
from django.conf import settings
from jwt.exceptions import InvalidSignatureError, ExpiredSignatureError

from core.utils.date import date_now_plus_delta_in_minutes

BEARER = 'Bearer'


class JwtToken:
    @staticmethod
    def encode(payload: Dict) -> str:
        payload['exp'] = date_now_plus_delta_in_minutes(1)
        encoded_jwt = jwt.encode(payload, settings.JWT_SECRET, algorithm="HS256")
        return f"{BEARER} {encoded_jwt}"

    @staticmethod
    def decode(token: str) -> Dict:
        encoded_token = token.split(BEARER)[1].strip()
        with contextlib.suppress(InvalidSignatureError, ExpiredSignatureError):
            return jwt.decode(encoded_token, settings.JWT_SECRET, algorithms=["HS256"])
