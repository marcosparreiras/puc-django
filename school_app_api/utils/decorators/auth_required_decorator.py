from typing import Callable, Any
from django.http import HttpResponse, HttpRequest
from django.template import loader
from ..assertions.assert_authentication import assertAuthentication
from ..exceptions.unauthorized_exception import UnauthorizedException


def authRequired(
    view: Callable[[HttpRequest, Any], HttpResponse]
) -> Callable[[HttpRequest, Any], HttpResponse]:
    def wrapper(request: HttpRequest, **kwargs: Any):
        try:
            assertAuthentication(request)
            return view(request, **kwargs)
        except UnauthorizedException:
            template = loader.get_template("login.html")
            return HttpResponse(template.render(None, request))

    return wrapper
