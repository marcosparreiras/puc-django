from faker import Faker
from typing import Optional
from school_app_api.models.student_model import Student


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
