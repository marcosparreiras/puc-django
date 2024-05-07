from typing import Callable, Any
from rest_framework.response import Response
from rest_framework.request import Request
from ..assertions.assert_authentication_and_get_user_id import (
    assertAuthenticationAndGetUserId,
)


def restAuthRequired(
    controller: Callable[[Request, Any], Response]
) -> Callable[[Request, Any], Response]:
    def wrapper(request: Request, **kwargs: Any) -> Response:
        userId = assertAuthenticationAndGetUserId(request)
        request.userId = userId
        return controller(request, **kwargs)

    return wrapper
