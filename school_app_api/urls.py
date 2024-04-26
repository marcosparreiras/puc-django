from django.urls import path
from . import views


urlpatterns = [
    # Template API
    path("app/", views.appView),
    # REST API
    path("student/", views.studentView),
    path("student/<int:student_code>", views.studentCodeView),
]
