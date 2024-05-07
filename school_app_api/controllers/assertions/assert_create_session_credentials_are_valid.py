import os
from typing import Optional
from ..exceptions.unauthorized_exception import UnauthorizedException
from ..exceptions.invalid_request_payload_exception import (
    InvalidRequestPayloadException,
)


def assertCreateSessionCredentialsAreValid(
    email: Optional[str], password: Optional[str]
) -> int:
    if email is None or password is None:
        raise InvalidRequestPayloadException(
            {"error": "email and passowrd are required fields"}
        )

    if email != os.environ.get("ADMIN_EMAIL") or password != os.environ.get(
        "ADMIN_PASSWORD"
    ):
        raise UnauthorizedException()

    userId = 1
    return userId
