from django.urls import path
from . import views_template_api
from . import views_rest_api


urlpatterns = [
    # Template API
    path("student/app/home", views_template_api.templateStudentLitView),
    path("student/app/create", views_template_api.templateStudentCreateView),
    # REST API
    path("student/", views_rest_api.restStudentView),
    path("student/<int:student_code>", views_rest_api.restStudentCodeView),
]
