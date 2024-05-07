from typing import Callable, Any
from django.http import HttpResponse, HttpRequest
from django.template import loader
from ..assertions.assert_authentication_and_get_user_id import (
    assertAuthenticationAndGetUserId,
)
from ..exceptions.unauthorized_exception import UnauthorizedException


def templateAuthRequired(
    view: Callable[[HttpRequest, Any], HttpResponse]
) -> Callable[[HttpRequest, Any], HttpResponse]:
    def wrapper(request: HttpRequest, **kwargs: Any) -> HttpResponse:
        try:
            userId = assertAuthenticationAndGetUserId(request)
            request.userId = userId
            return view(request, **kwargs)
        except UnauthorizedException:
            template = loader.get_template("login.html")
            return HttpResponse(template.render(None, request))

    return wrapper
