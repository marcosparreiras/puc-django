from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from ..controllers.create_student_controller import createStudentController
from ..controllers.list_students_controller import listStudentsController
from ..controllers.get_student_controller import getStudentController
from ..controllers.update_student_controller import updateStudentController
from ..controllers.delete_student_controller import deleteStudentController
from ..controllers._global_controller_handler import globalControllerHandler


@api_view(["POST", "GET"])
def restStudentView(request: Request) -> Response:
    controllers = {
        "POST": createStudentController,
        "GET": listStudentsController,
    }
    response = globalControllerHandler(request, controllers)
    return response


@api_view(["GET", "PUT", "DELETE"])
def restStudentCodeView(request: Request, student_code: int) -> Response:
    controllers = {
        "GET": getStudentController,
        "PUT": updateStudentController,
        "DELETE": deleteStudentController,
    }
    response = globalControllerHandler(request, controllers, student_code=student_code)
    return response
