import json
from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from .factories.student_factory import studenteFactory


class RestApiTestE2e(TestCase):
    client = Client()

    def setUp(self):
        call_command("flush", interactive=False, verbosity=0)

    def test_list_students(self) -> None:
        for _ in range(15):
            studenteFactory()
        response = self.client.get("/api/student/")
        responseBody = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(responseBody["students"]), 15)
