from django.db import models
import datetime
import uuid 

class User(models.Model):
    id = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False)
    name = models.CharField(max_length=80, null=False)
    date_of_birth = models.DateField(null=False)
    address_street = models.CharField(max_length=80, null=False)
    address_number = models.IntegerField(null= False)
    registration_number = models.IntegerField(null=True)
    is_principal = models.BooleanField(null=True)
    is_employee = models.CharField(null=True)
    is_student = models.CharField(null=True)
    updated_at = models.DateField(null=True)
    created_at = models.DateField(default=datetime.date.today)

    def __str__(self):
        return f"({self.id}) {self.name}"

