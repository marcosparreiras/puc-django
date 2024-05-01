from django.template import loader
from django.http import HttpResponse, HttpRequest
from ..models.student_model import Student


def templateStudentLitView(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("student-list.html")
    context = {"students": Student.objects.all()}
    return HttpResponse(template.render(context, request))


def templateStudentCreateView(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("student-create.html")
    return HttpResponse(template.render(None, request))


def templateStudentEditView(request: HttpRequest, student_code: int) -> HttpResponse:
    try:
        template = loader.get_template("student-edit.html")
        context = {"student": Student.objects.get(student_code=student_code)}
    except Student.DoesNotExist:
        template = loader.get_template("student-404.html")
        context = None
    finally:
        return HttpResponse(template.render(context, request))
