from django.db import models
from django.contrib.auth.models import User
import uuid


def is_employee(self):
    if self.employee:
        return True
    else:
        return False
    

User.add_to_class('employee', is_employee)

class Employee(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, related_name='employee', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    number = models.IntegerField()
    bithday = models.DateField(null = True, blank=True)
    is_emp = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    
    


