from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK
from ..models.student_model import Student
from .assertions.assert_student_exists import assertStudentExists


def getStudentController(_: Request, student_code: int) -> Response:
    student = Student.findByStudentCode(student_code)
    assertStudentExists(student, student_code)
    return Response({"student": student.getPresenter()}, status=HTTP_200_OK)
