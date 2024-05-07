import json
import jwt
import os
from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from school_app_api.models.student_model import Student
from .factories.student_factory import studenteFactory


class RestApiTestE2e(TestCase):
    client = Client()
    cookies = f"token={jwt.encode({"sub": 1}, os.environ.get("JWT_SECRET"), algorithm="HS256")}"

    def setUp(self):
        call_command("flush", interactive=False, verbosity=0)

    def test_delete_student(self) -> None:
        studenteFactory("Thomas Frank")
        self.client.cookies.load(self.cookies)
        response = self.client.delete("/api/student/1")
        self.assertEqual(response.status_code, 204)
        with self.assertRaises(Student.DoesNotExist):
            Student.objects.get(student_code=1)

    def test_delete_unexistest_student(self):
        self.client.cookies.load(self.cookies)
        response = self.client.delete("/api/student/1")
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data["message"], "Student (1) not found")

    def test_delete_without_token(self):
        studenteFactory("Thomas Frank")
        self.client.cookies.clear()
        response = self.client.delete("/api/student/1")
        self.assertEqual(response.status_code, 401)

