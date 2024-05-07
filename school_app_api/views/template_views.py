from django.template import loader
from django.http import HttpResponse, HttpRequest
from ..models.student_model import Student
from ..utils.decorators.template_auth_required_decorator import templateAuthRequired


@templateAuthRequired
def templateStudentLitView(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("student-list.html")
    context = {"students": Student.findMany()}
    return HttpResponse(template.render(context, request))


@templateAuthRequired
def templateStudentCreateView(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("student-create.html")
    return HttpResponse(template.render(None, request))


@templateAuthRequired
def templateStudentEditView(request: HttpRequest, student_code: int) -> HttpResponse:
    student = Student.findByStudentCode(student_code)
    if student is None:
        template = loader.get_template("student-404.html")
        return HttpResponse(template.render(None, request))
    template = loader.get_template("student-edit.html")
    context = {"student": student}
    return HttpResponse(template.render(context, request))
