from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_201_CREATED
from ..models.student_model import Student
from .serializers.create_student_request_serialiazer import (
    CreateStudentRequestSerialiazer,
)
from ..exceptions.invalid_request_payload_exception import (
    InvalidRequestPayloadException,
)


def createStudentController(request: Request) -> Response:
    requestPayload = CreateStudentRequestSerialiazer(data=request.data)
    if not requestPayload.is_valid():
        raise InvalidRequestPayloadException(requestPayload.errors)
    student_code = Student.create(
        name=requestPayload.data.get("name"),
        date_of_birth=requestPayload.data.get("date_of_birth"),
        address_street=requestPayload.data.get("address_street"),
        address_number=requestPayload.data.get("address_number"),
    )
    return Response(
        {"student_code": student_code},
        status=HTTP_201_CREATED,
    )
