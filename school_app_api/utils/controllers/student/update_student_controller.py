from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_204_NO_CONTENT
from ....models.student_model import Student
from ...assertions.assert_student_exists import assertStudentExists
from ...decorators.rest_auth_required_decorator import restAuthRequired
from ...assertions.assert_authentication_and_get_user_id import (
    assertAuthenticationAndGetUserId,
)
from ...serializers.update_student_request_serializer import (
    UpdateStudentRequestSerializer,
)
from ...assertions.assert_request_payload_is_valid_and_get_serialized_data import (
    assertRequestPayloadIsValidAndGetSerializedData,
)


@restAuthRequired
def updateStudentController(request: Request, student_code: int) -> Response:
    requestPayload = assertRequestPayloadIsValidAndGetSerializedData(
        request.data, UpdateStudentRequestSerializer
    )
    student = Student.findByStudentCode(student_code)
    assertStudentExists(student, student_code)
    student.name = requestPayload.get("name")
    student.date_of_birth = requestPayload.get("date_of_birth")
    student.address_street = requestPayload.get("address_street")
    student.address_number = requestPayload.get("address_number")
    student.save()
    return Response(None, status=HTTP_204_NO_CONTENT)
