from django.http import HttpResponse
from django.template import loader

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request

from .models import Student
from . import serizalizers


# Template views


def templateStudentLitView(request):
    template = loader.get_template("student-list.html")
    context = {"students": Student.objects.all()}
    return HttpResponse(template.render(context, request))


def templateStudentCreateView(_):
    template = loader.get_template("student-create.html")
    return HttpResponse(template.render())


# REST views


@api_view(["POST", "GET"])
def restStudentView(request: Request) -> Response:
    controllers = {"POST": createStudent, "GET": listStudents}
    try:
        response = controllers[request.method](request)
        return response
    except Exception:
        return Response(
            {"message": "Internal server error"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@api_view(["GET", "PUT", "DELETE"])
def restStudentCodeView(request: Request, student_code: int) -> Response:
    controllers = {"GET": getStudent, "PUT": updateStudent, "DELETE": deleteStudent}
    try:
        response = controllers[request.method](request, student_code)
        return response
    except Exception:
        return Response(
            {"message": "Internal server error"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


# REST Controllers


def createStudent(request: Request) -> Response:
    serializedRequestData = serizalizers.StudentModelCreateRequestSerializer(
        data=request.data
    )

    if not serializedRequestData.is_valid():
        return Response(
            {"message": serializedRequestData.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
    student = Student.objects.create(
        name=serializedRequestData.data.get("name"),
        date_of_birth=serializedRequestData.data.get("date_of_birth"),
        address_street=serializedRequestData.data.get("address_street"),
        address_number=serializedRequestData.data.get("address_number"),
    )
    serializedStudent = serizalizers.StudentModelPresenterSerializer(student)
    return Response(
        {"student_code": serializedStudent.data.get("student_code")},
        status=status.HTTP_201_CREATED,
    )


def listStudents(_: Request) -> Response:
    students = Student.objects.all()
    serializedStudents = serizalizers.StudentModelPresenterSerializer(
        students, many=True
    )
    return Response({"students": serializedStudents.data}, status=status.HTTP_200_OK)


def getStudent(_: Request, student_code: int) -> Response:
    try:
        student = Student.objects.get(student_code=student_code)
        serializedStudent = serizalizers.StudentModelPresenterSerializer(student)
        return Response({"student": serializedStudent.data}, status=status.HTTP_200_OK)
    except Student.DoesNotExist:
        return Response(
            {"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND
        )


def updateStudent(request: Request, student_code: int) -> Response:
    serializedRequestData = serizalizers.StudentModelUpdateRequestSerializer(
        data=request.data
    )
    if not serializedRequestData.is_valid():
        return Response(
            {"message": serializedRequestData.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )
    try:
        student = Student.objects.get(student_code=student_code)
        student.name = serializedRequestData.data.get("name")
        student.date_of_birth = serializedRequestData.data.get("date_of_birth")
        student.address_street = serializedRequestData.data.get("address_street")
        student.address_number = serializedRequestData.data.get("address_number")
        student.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
        return Response(
            {"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND
        )


def deleteStudent(_: Request, student_code: int) -> Response:
    try:
        student = Student.objects.get(student_code=student_code)
        student.delete()
        return Response({}, status=status.HTTP_204_NO_CONTENT)
    except Student.DoesNotExist:
        return Response(
            {"message": "Student not found"}, status=status.HTTP_404_NOT_FOUND
        )
