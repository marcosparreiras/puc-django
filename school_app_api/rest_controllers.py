from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from .models import Student
from .exceptions import InvalidRequestPayloadException, StudentNotFoundException
from .serizalizers import (
    StudentModelPresenterSerializer,
    StudentModelCreateRequestSerializer,
    StudentModelUpdateRequestSerializer,
)


def createStudent(request: Request) -> Response:
    requestPayload = StudentModelCreateRequestSerializer(data=request.data)
    if not requestPayload.is_valid():
        raise InvalidRequestPayloadException(requestPayload.errors)
    student = Student.objects.create(
        name=requestPayload.data.get("name"),
        date_of_birth=requestPayload.data.get("date_of_birth"),
        address_street=requestPayload.data.get("address_street"),
        address_number=requestPayload.data.get("address_number"),
    )
    studentPresenter = StudentModelPresenterSerializer(student)
    return Response(
        {"student_code": studentPresenter.data.get("student_code")},
        status=HTTP_201_CREATED,
    )


def listStudents(_: Request) -> Response:
    students = Student.objects.all()
    studentsPresenter = StudentModelPresenterSerializer(students, many=True)
    return Response({"students": studentsPresenter.data}, status=HTTP_200_OK)


def getStudent(_: Request, student_code: int) -> Response:
    try:
        student = Student.objects.get(student_code=student_code)
    except Student.DoesNotExist:
        raise StudentNotFoundException(student_code)
    studentPresenter = StudentModelPresenterSerializer(student)
    return Response({"student": studentPresenter.data}, status=HTTP_200_OK)


def updateStudent(request: Request, student_code: int) -> Response:
    requestPayload = StudentModelUpdateRequestSerializer(data=request.data)
    if not requestPayload.is_valid():
        raise InvalidRequestPayloadException(requestPayload.errors)
    try:
        student = Student.objects.get(student_code=student_code)
    except Student.DoesNotExist:
        raise StudentNotFoundException(student_code)
    student.name = requestPayload.data.get("name")
    student.date_of_birth = requestPayload.data.get("date_of_birth")
    student.address_street = requestPayload.data.get("address_street")
    student.address_number = requestPayload.data.get("address_number")
    student.save()
    return Response(None, status=HTTP_204_NO_CONTENT)


def deleteStudent(_: Request, student_code: int) -> Response:
    try:
        student = Student.objects.get(student_code=student_code)
    except Student.DoesNotExist:
        raise StudentNotFoundException(student_code)
    student.delete()
    return Response(None, status=HTTP_204_NO_CONTENT)
