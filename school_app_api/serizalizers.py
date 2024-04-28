from rest_framework import serializers
from .models import Student


class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "student_code",
            "name",
            "date_of_birth",
            "created_at",
            "address_street",
            "address_number",
        ]


class StudentModelPresenterSerializer(StudentModelSerializer):
    pass


class StudentModelCreateRequestSerializer(StudentModelSerializer):
    class Meta(StudentModelSerializer.Meta):
        fields = [
            "name",
            "date_of_birth",
            "address_street",
            "address_number",
        ]


class StudentModelUpdateRequestSerializer(StudentModelCreateRequestSerializer):
    pass
