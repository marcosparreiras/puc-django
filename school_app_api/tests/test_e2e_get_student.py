import json
import jwt
from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from .factories.student_factory import studenteFactory


class RestApiTestE2e(TestCase):
    client = Client()
    cookies = f"token={jwt.encode({"sub": 1}, "default", algorithm="HS256")}"


    def setUp(self):
        call_command("flush", interactive=False, verbosity=0)

    def test_get_student(self) -> None:
        name = "John Doe"
        studenteFactory(name)
        self.client.cookies.load(self.cookies)
        response = self.client.get("/api/student/1")
        responseBody = json.loads(response.content.decode("utf-8"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(responseBody["student"]["name"], name)

    def test_get_unexistent_student(self) -> None:
        self.client.cookies.load(self.cookies)
        response = self.client.get("/api/student/1")
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data["message"], "Student (1) not found")

    def test_get_student_without_token(self) -> None:
        name = "John Doe"
        studenteFactory(name)
        self.client.cookies.clear()
        response = self.client.get("/api/student/1")
        self.assertEqual(response.status_code, 401)
        
