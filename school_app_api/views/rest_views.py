from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from ..utils.controllers.student.create_student_controller import (
    createStudentController,
)
from ..utils.controllers.student.list_students_controller import listStudentsController
from ..utils.controllers.student.get_student_controller import getStudentController
from ..utils.controllers.student.update_student_controller import (
    updateStudentController,
)
from ..utils.controllers.student.delete_student_controller import (
    deleteStudentController,
)
from ..utils.controllers.session.create_session_controller import (
    createSessionController,
)
from ..utils.controllers.session.delete_session_controller import (
    deleteSessionController,
)
from ..utils.decorators.rest_error_handler_decorator import restErrorHandler


@api_view(["POST", "DELETE"])
def sessionView(request: Request) -> Response:
    controllers = {"POST": createSessionController, "DELETE": deleteSessionController}
    return restErrorHandler(controllers[request.method])(request)


@api_view(["POST", "GET"])
def restStudentView(request: Request) -> Response:
    controllers = {
        "POST": createStudentController,
        "GET": listStudentsController,
    }
    return restErrorHandler(controllers[request.method])(request)


@api_view(["GET", "PUT", "DELETE"])
def restStudentCodeView(request: Request, student_code: int) -> Response:
    controllers = {
        "GET": getStudentController,
        "PUT": updateStudentController,
        "DELETE": deleteStudentController,
    }
    return restErrorHandler(controllers[request.method])(
        request, student_code=student_code
    )
