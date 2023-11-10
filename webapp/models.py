from django.db import models
from django.contrib.auth.models import AbstractUser

class StaffRecords(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    employee_id = models.CharField(max_length=20, unique=True)  # Employee ID
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100,unique=True)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class StudentRecords(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    student_id = models.CharField(max_length=20, unique=True)  # student ID
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    tutor = models.CharField(max_length=50)
    parent_phone = models.CharField(max_length=15)
    parent_name = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class ParentRecords(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    number_of_childrens = models.IntegerField(max_length=20) 
    students_ids = models.ManyToManyField('StudentRecords')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100,unique=True)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

