from django.template import loader
from django.http import HttpResponse, HttpRequest
from .models import Student


def templateStudentLitView(request: HttpRequest) -> HttpResponse:
    template = loader.get_template("student-list.html")
    context = {"students": Student.objects.all()}
    return HttpResponse(template.render(context, request))


def templateStudentCreateView(_: HttpRequest) -> HttpResponse:
    template = loader.get_template("student-create.html")
    return HttpResponse(template.render())
