from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK
from ..models.student_model import Student
from ..exceptions.student_not_found_exception import StudentNotFoundException


def getStudentController(_: Request, student_code: int) -> Response:
    student = Student.findByStudentCode(student_code)
    if student is None:
        raise StudentNotFoundException(student_code)
    return Response({"student": student.getPresenter()}, status=HTTP_200_OK)
