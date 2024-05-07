from django.template import loader
from django.http import HttpResponse, HttpRequest
from ..models.student_model import Student
from ..utils.decorators.auth_required_decorator import authRequired


@authRequired
def templateStudentLitView(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("student-list.html")
    context = {"students": Student.findAll()}
    return HttpResponse(template.render(context, request))


@authRequired
def templateStudentCreateView(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("student-create.html")
    return HttpResponse(template.render(None, request))


@authRequired
def templateStudentEditView(request: HttpRequest, student_code: int) -> HttpResponse:
    student = Student.findByStudentCode(student_code)
    if student is None:
        template = loader.get_template("student-404.html")
        return HttpResponse(template.render(None, request))
    template = loader.get_template("student-edit.html")
    context = {"student": student}
    return HttpResponse(template.render(context, request))
