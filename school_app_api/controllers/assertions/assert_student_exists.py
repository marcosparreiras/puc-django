from typing import Optional
from ...models.student_model import Student
from ..exceptions.student_not_found_exception import StudentNotFoundException


def assertStudentExists(student: Optional[Student], student_identifier: str) -> None:
    if not isinstance(student, Student):
        raise StudentNotFoundException(student_identifier)
