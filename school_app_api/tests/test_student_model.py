from django.test import TestCase
from django.utils import timezone
from django.core.management import call_command
from school_app_api.models.student_model import Student


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
