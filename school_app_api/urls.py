from django.urls import path
from .views.rest_views import restStudentView, restStudentCodeView, sessionView
from .views.template_views import (
    templateStudentLitView,
    templateStudentCreateView,
    templateStudentEditView,
)


urlpatterns = [
    # REST API
    path("session/", sessionView),
    path("student/", restStudentView),
    path("student/<int:student_code>", restStudentCodeView),
    # Template API
    path("student/app/home", templateStudentLitView),
    path("student/app/create", templateStudentCreateView),
    path(
        "student/app/edit/<int:student_code>",
        templateStudentEditView,
    ),
]
