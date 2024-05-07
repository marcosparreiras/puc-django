from django.test import TestCase
from django.test import Client
from django.core.management import call_command


class RestApiTestE2e(TestCase):
    client = Client()

    def setUp(self):
        call_command("flush", interactive=False, verbosity=0)

    def test_delete_session(self) -> None:
        response = self.client.delete("/api/session/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.cookies.get("token").value, "")
