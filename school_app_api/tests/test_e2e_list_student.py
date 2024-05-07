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

    def test_list_students(self) -> None:
        for _ in range(15):
            studenteFactory()
        self.client.cookies.load(self.cookies)
        response = self.client.get("/api/student/")
        responseBody = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(responseBody["students"]), 15)

    def test_list_students_without_token(self) -> None:
        for _ in range(15):
            studenteFactory()
        self.client.cookies.clear()
        response = self.client.get("/api/student/")
        self.assertEqual(response.status_code, 401)

