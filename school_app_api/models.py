from django.db import models


class Student(models.Model):
    student_code = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80, null=False)
    date_of_birth = models.DateField(null=False)
    created_at = models.DateField(auto_now=True)
    address_street = models.CharField(max_length=80, null=False)
    address_number = models.IntegerField(null=False)

    def __str__(self):
        return f"({self.student_code}) {self.name}"
