from django.urls import path
from . import views


urlpatterns = [
    path("student/", views.studentView),
    path("student/<int:student_code>", views.studentCodeView),
]
