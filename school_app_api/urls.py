from django.urls import path
from . import views


urlpatterns = [
    # Template API
    path("student/app/home", views.templateStudentLitView),
    path("student/app/create", views.templateStudentCreateView),
    # REST API
    path("student/", views.restStudentView),
    path("student/<int:student_code>", views.restStudentCodeView),
]
