import jwt
import os
from django.http import HttpRequest
from ..exceptions.unauthorized_exception import UnauthorizedException


def assertAuthenticationAndGetUserId(request: HttpRequest) -> int:
    token = request.COOKIES.get("token")
    if token is None:
        raise UnauthorizedException()
    try:
        payload = jwt.decode(token, os.environ.get("JWT_SECRET"), algorithms=["HS256"])
        return payload.get("sub")
    except Exception:
        raise UnauthorizedException()
