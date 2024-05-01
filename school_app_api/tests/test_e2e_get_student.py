import json
from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from .factories.student_factory import studenteFactory


class RestApiTestE2e(TestCase):
    client = Client()

    def setUp(self):
        call_command("flush", interactive=False, verbosity=0)

    def test_get_student(self) -> None:
        name = "John Doe"
        studenteFactory(name)
        response = self.client.get("/api/student/1")
        responseBody = json.loads(response.content.decode("utf-8"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(responseBody["student"]["name"], name)

    def test_get_unexistent_student(self):
        response = self.client.get("/api/student/1")
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data["message"], "Student (1) not found")
