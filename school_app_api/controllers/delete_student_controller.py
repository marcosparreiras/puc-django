from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_204_NO_CONTENT
from ..models.student_model import Student
from ..exceptions.student_not_found_exception import StudentNotFoundException


def deleteStudentController(_: Request, student_code: int) -> Response:
    student = Student.findByStudentCode(student_code)
    if student is None:
        raise StudentNotFoundException(student_code)
    student.delete()
    return Response(None, status=HTTP_204_NO_CONTENT)
