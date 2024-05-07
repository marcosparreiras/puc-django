from typing import Optional, List, Any
from django.db import models
from datetime import date


class Student(models.Model):
    student_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, null=False)
    date_of_birth = models.DateField(null=False)
    created_at = models.DateField(auto_now=True)
    address_street = models.CharField(max_length=80, null=False)
    address_number = models.IntegerField(null=False)

    @staticmethod
    def findMany(**kwargs: Any) -> List["Student"]:
        students = Student.objects.all().order_by("-created_at")
        if len(kwargs) <= 0:
            return students
        kwargs_conteins = {
            f"{chave}__icontains": valor for chave, valor in kwargs.items()
        }
        return students.filter(**kwargs_conteins)

    @staticmethod
    def findByStudentCode(student_code: int) -> Optional["Student"]:
        try:
            student = Student.objects.get(student_code=student_code)
            return student
        except Student.DoesNotExist:
            return None

    @staticmethod
    def create(
        name: str, date_of_birth: date, address_street: str, address_number: int
    ) -> int:
        stundet = Student.objects.create(
            name=name,
            date_of_birth=date_of_birth,
            address_street=address_street,
            address_number=address_number,
        )
        return stundet.student_code

    def getPresenter(self) -> dict:
        return {
            "student_code": self.student_code,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "created_at": self.created_at,
            "address_street": self.address_street,
            "address_number": self.address_number,
        }

    def __str__(self) -> str:
        return f"({self.student_code}) {self.name}"
