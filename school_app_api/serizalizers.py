from rest_framework import serializers
from .models import Student


class StudentModelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "name",
            "date_of_birth",
            "address_street",
            "address_number",
        ]


class StudentModelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = [
            "name",
            "date_of_birth",
            "address_street",
            "address_number",
        ]


class StudentModelShowSerializer(serializers.ModelSerializer):
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
