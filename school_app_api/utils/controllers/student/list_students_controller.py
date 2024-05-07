from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK
from ....models.student_model import Student
from ...decorators.rest_auth_required_decorator import restAuthRequired


@restAuthRequired
def listStudentsController(request: Request) -> Response:
    nameFilter = request.query_params.get("name", "")
    addressStreetFilter = request.query_params.get("address_street", "")
    studentCodeFilter = request.query_params.get("student_code", "")
    addressNumberFilter = request.query_params.get("address_number", "")

    students = Student.findMany(
        name=nameFilter,
        address_street=addressStreetFilter,
        student_code=studentCodeFilter,
        address_number=addressNumberFilter,
    )

    studentsPresenter = [student.getPresenter() for student in students]
    return Response({"students": studentsPresenter}, status=HTTP_200_OK)
