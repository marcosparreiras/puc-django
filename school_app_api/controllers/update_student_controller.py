from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_204_NO_CONTENT
from ..models.student_model import Student
from ..exceptions.student_not_found_exception import StudentNotFoundException
from ..exceptions.invalid_request_payload_exception import (
    InvalidRequestPayloadException,
)
from .serializers.update_student_request_serializer import (
    UpdateStudentRequestSerializer,
)


def updateStudentController(request: Request, student_code: int) -> Response:
    requestPayload = UpdateStudentRequestSerializer(data=request.data)
    if not requestPayload.is_valid():
        raise InvalidRequestPayloadException(requestPayload.errors)
    student = Student.findByStudentCode(student_code)
    if student is None:
        raise StudentNotFoundException(student_code)
    student.name = requestPayload.data.get("name")
    student.date_of_birth = requestPayload.data.get("date_of_birth")
    student.address_street = requestPayload.data.get("address_street")
    student.address_number = requestPayload.data.get("address_number")
    student.save()
    return Response(None, status=HTTP_204_NO_CONTENT)
