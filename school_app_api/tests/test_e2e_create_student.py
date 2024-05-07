import json
import jwt
from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from school_app_api.models.student_model import Student


class RestApiTestE2e(TestCase):
    client = Client()
    cookies = f"token={jwt.encode({"sub": 1}, "default", algorithm="HS256")}"

    def setUp(self):
        call_command("flush", interactive=False, verbosity=0)

    def test_create_student(self) -> None:
        data = {
            "name": "John Doe",
            "date_of_birth": "1990-05-15",
            "address_street": "Pine Street West",
            "address_number": 45,
        }
        data_json = json.dumps(data)
        self.client.cookies.load(self.cookies)
        response = self.client.post(
            "/api/student/", data=data_json, content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        studentOnDatabase = Student.objects.first()
        self.assertEqual(studentOnDatabase.name, data["name"])

    def test_create_student_with_invalid_payload(self):
        data = {
            "name": "John Doe",
            "date_of_birth": "1990-05-15",
            "address_street": "Pine Street West",
        }
        data_json = json.dumps(data)
        self.client.cookies.load(self.cookies)
        response = self.client.post(
            "/api/student/", data=data_json, content_type="application/json"
        )
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data["message"], "Invalid request payload")

    def test_create_student_without_token(self):
        data = {
             "name": "John Doe",
            "date_of_birth": "1990-05-15",
            "address_street": "Pine Street West",
            "address_number": 45,
        }
        data_json = json.dumps(data)
        self.client.cookies.clear()
        response = self.client.post(
            "/api/student/", data=data_json, content_type="application/json"
        )
        self.assertEqual(response.status_code, 401)
