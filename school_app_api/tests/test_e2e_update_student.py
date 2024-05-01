import json
from django.test import TestCase
from django.test import Client
from django.core.management import call_command
from school_app_api.models.student_model import Student
from .factories.student_factory import studenteFactory


class RestApiTestE2e(TestCase):
    client = Client()

    def setUp(self):
        call_command("flush", interactive=False, verbosity=0)

    def test_update_student(self) -> None:
        student = studenteFactory("Thomas Frank")
        data = {
            "name": "John Doe",
            "date_of_birth": str(student.date_of_birth),
            "address_street": student.address_street,
            "address_number": student.address_number,
        }
        data_json = json.dumps(data)
        response = self.client.put(
            "/api/student/1", data=data_json, content_type="application/json"
        )
        self.assertEqual(response.status_code, 204)
        studentOnDatabase = Student.objects.get(student_code=1)
        self.assertEqual(studentOnDatabase.name, data["name"])

    def test_update_student_with_invalid_payload(self):
        studenteFactory(name="Thomas Frank")
        data = {
            "name": "John Doe",
            "date_of_birth": "1990-05-15",
            "address_street": "Pine Street West",
        }
        data_json = json.dumps(data)
        response = self.client.put(
            "/api/student/1", data=data_json, content_type="application/json"
        )
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data["message"], "Invalid request payload")

    def test_update_unexistest_student(self):
        data = {
            "name": "John Doe",
            "date_of_birth": "1990-05-15",
            "address_street": "Pine Street West",
            "address_number": 45,
        }
        data_json = json.dumps(data)
        response = self.client.put(
            "/api/student/1", data=data_json, content_type="application/json"
        )
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data["message"], "Student (1) not found")
