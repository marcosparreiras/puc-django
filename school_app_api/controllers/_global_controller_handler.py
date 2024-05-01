from typing import Dict, Callable
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from rest_framework.response import Response
from rest_framework.request import Request

from ..exceptions.invalid_request_payload_exception import (
    InvalidRequestPayloadException,
)
from ..exceptions.student_not_found_exception import StudentNotFoundException


def globalControllerHandler(
    request: Request,
    controllers: Dict[str, Callable[[Request], Response]],
    **kwargs: Dict[str, any]
) -> Response:
    try:
        response = controllers[request.method](request, **kwargs)
        return response
    except StudentNotFoundException as exception:
        return Response({"message": str(exception)}, status=HTTP_404_NOT_FOUND)
    except InvalidRequestPayloadException as exception:
        return Response(
            {
                "message": str(exception),
                "errors": exception.getErrors(),
            },
            status=HTTP_400_BAD_REQUEST,
        )
    except Exception:
        return Response(
            {"message": "Internal server error"},
            status=HTTP_500_INTERNAL_SERVER_ERROR,
        )
