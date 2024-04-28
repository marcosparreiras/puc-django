import json
from typing import Optional
from faker import Faker
from django.test import TestCase
from django.utils import timezone
from django.test import Client
from django.core.management import call_command
from .models import Student


def studenteFactory(
    name: Optional[str] = None,
) -> Student:
    faker = Faker()
    name = faker.name() if name is None else name
    student = Student.objects.create(
        name=name,
        date_of_birth=faker.date_of_birth(minimum_age=15, maximum_age=50),
        address_street=faker.street_address(),
        address_number=faker.random_int(min=1, max=1000),
    )
    return student


class StudentModelTests(TestCase):
    def setUp(self):
        call_command("flush", interactive=False, verbosity=0)

    def test_auto_assign_student_code_and_created_at_upon_creation(
        self,
    ) -> None:
        student = Student.objects.create(
            name="John Doe",
            date_of_birth="1990-05-15",
            address_street="Pine Street West",
            address_number=45,
        )
        self.assertEqual(student.student_code, 1)
        self.assertTrue(student.created_at == timezone.now().date())


class RestApiTestE2e(TestCase):
    client = Client()
    base_url = "http://localhost:8000/api/"

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
        response = self.client.post(
            "/api/student/", data=data_json, content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)
        studentOnDatabase = Student.objects.first()
        self.assertEqual(studentOnDatabase.name, data["name"])

    def test_list_students(self) -> None:
        for _ in range(15):
            studenteFactory()
        response = self.client.get("/api/student/")
        responseBody = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(responseBody["students"]), 15)

    def test_get_student(self) -> None:
        name = "John Doe"
        studenteFactory(name)
        response = self.client.get("/api/student/1")
        responseBody = json.loads(response.content.decode("utf-8"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(responseBody["student"]["name"], name)

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

    def test_delete_student(self) -> None:
        studenteFactory("Thomas Frank")
        response = self.client.delete("/api/student/1")
        self.assertEqual(response.status_code, 204)
        with self.assertRaises(Student.DoesNotExist):
            Student.objects.get(student_code=1)

    def test_create_student_with_invalid_payload(self):
        data = {
            "name": "John Doe",
            "date_of_birth": "1990-05-15",
            "address_street": "Pine Street West",
        }
        data_json = json.dumps(data)
        response = self.client.post(
            "/api/student/", data=data_json, content_type="application/json"
        )
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response_data["message"], "Invalid request payload")

    def test_get_unexistent_student(self):
        response = self.client.get("/api/student/1")
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data["message"], "Student (1) not found")

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

    def test_delete_unexistest_student(self):
        response = self.client.delete("/api/student/1")
        response_data = json.loads(response.content.decode("utf-8"))
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response_data["message"], "Student (1) not found")
