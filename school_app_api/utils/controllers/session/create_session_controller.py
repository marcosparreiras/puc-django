import jwt
import os
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_201_CREATED
from ...assertions.assert_credentials_are_valid_and_get_user_id import (
    assertCredentialsAreValidAndGetUserId,
)


def createSessionController(request: Request) -> Response:
    email = request.data.get("email")
    password = request.data.get("password")
    userId = assertCredentialsAreValidAndGetUserId(email, password)

    tokenPayload = {"sub": userId}
    token = jwt.encode(tokenPayload, os.environ.get("JWT_SECRET"), algorithm="HS256")

    response = Response()
    response.set_cookie(key="token", value=token, httponly=True)
    response.status_code = HTTP_201_CREATED
    return response
