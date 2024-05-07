from rest_framework import serializers
from ...models.student_model import Student


class CreateStudentRequestSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "name",
            "date_of_birth",
            "address_street",
            "address_number",
        ]
