from typing import Dict

import requests
from rest_framework.response import Response


def post(url: str, payload: Dict, headers: Dict) -> Response:
    response = requests.post(url=url, data=payload, headers=headers)
    return Response(status=response.status_code)
