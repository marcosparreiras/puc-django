from typing import Dict, Callable
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR,
)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .exceptions import InvalidRequestPayloadException, StudentNotFoundException
from . import rest_controllers


@api_view(["POST", "GET"])
def restStudentView(request: Request) -> Response:
    controllers = {
        "POST": rest_controllers.createStudent,
        "GET": rest_controllers.listStudents,
    }
    response = restViewHandler(request, controllers)
    return response


@api_view(["GET", "PUT", "DELETE"])
def restStudentCodeView(request: Request, student_code: int) -> Response:
    controllers = {
        "GET": rest_controllers.getStudent,
        "PUT": rest_controllers.updateStudent,
        "DELETE": rest_controllers.deleteStudent,
    }
    response = restViewHandler(request, controllers, student_code=student_code)
    return response


def restViewHandler(
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
