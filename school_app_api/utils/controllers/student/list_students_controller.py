from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK
from ....models.student_model import Student
from ...assertions.assert_authentication import assertAuthentication


def listStudentsController(request: Request) -> Response:
    assertAuthentication(request)
    students = Student.findAll()
    studentsPresenter = [student.getPresenter() for student in students]
    return Response({"students": studentsPresenter}, status=HTTP_200_OK)
