import json
import jwt
import os
from django.test import TestCase
from django.test import Client
from django.core.management import call_command


class RestApiTestE2e(TestCase):
    client = Client()

    def setUp(self):
        call_command("flush", interactive=False, verbosity=0)

    def test_create_session(self) -> None:
        data = {
            "email": os.environ.get("ADMIN_EMAIL"),
            "password": os.environ.get("ADMIN_PASSWORD"),
        }
        data_json = json.dumps(data)
        response = self.client.post(
            "/api/session/", data=data_json, content_type="application/json"
        )

        self.assertEqual(response.status_code, 201)
        jwt.decode(
            response.cookies.get("token").value,
            os.environ.get("JWT_SECRET"),
            algorithms=["HS256"],
        )

    def test_create_session_with_invalid_data(self) -> None:
        data = {
            "email": "johndoe@example.com",
            "password": "654321",
        }
        data_json = json.dumps(data)
        response = self.client.post(
            "/api/session/", data=data_json, content_type="application/json"
        )

        self.assertEqual(response.status_code, 401)
