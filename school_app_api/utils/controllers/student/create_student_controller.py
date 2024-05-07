from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_201_CREATED
from ....models.student_model import Student
from ...decorators.rest_auth_required_decorator import restAuthRequired
from ...serializers.create_student_request_serialiazer import (
    CreateStudentRequestSerialiazer,
)
from ...assertions.assert_request_payload_is_valid_and_get_serialized_data import (
    assertRequestPayloadIsValidAndGetSerializedData,
)


@restAuthRequired
def createStudentController(request: Request) -> Response:
    requestPayload = assertRequestPayloadIsValidAndGetSerializedData(
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
