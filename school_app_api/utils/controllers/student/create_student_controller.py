from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_201_CREATED
from ....models.student_model import Student
from ...assertions.assert_request_payload_is_valid import assertRequestPayloadIsValid
from ...assertions.assert_authentication import assertAuthentication
from ...serializers.create_student_request_serialiazer import (
    CreateStudentRequestSerialiazer,
)


def createStudentController(request: Request) -> Response:
    assertAuthentication(request)
    requestPayload = assertRequestPayloadIsValid(
        request.data, CreateStudentRequestSerialiazer
    )
    student_code = Student.create(
        name=requestPayload.get("name"),
        date_of_birth=requestPayload.get("date_of_birth"),
        address_street=requestPayload.get("address_street"),
        address_number=requestPayload.get("address_number"),
    )
    return Response(
        {"student_code": student_code},
        status=HTTP_201_CREATED,
    )
