from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_staff_member = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)

    def __str__(self):
        return self.email

class Student(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    student_id = models.CharField(max_length=10, unique=True)
    # Add other student-related fields as needed

    def __str__(self):
        return f"{self.user.email} (Student)"

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    employee_id = models.CharField(max_length=10, unique=True)
    # Add other staff-related fields as needed

    def __str__(self):
        return f"{self.user.email} (Staff)"

class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Add other admin-related fields as needed

    def __str__(self):
        return f"{self.user.email} (Admin)"

class Parent(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    # Add other parent-related fields as needed

    def __str__(self):
        return f"{self.user.email} (Parent)"



class Record(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	first_name = models.CharField(max_length=50)
	last_name =  models.CharField(max_length=50)
	email =  models.CharField(max_length=100)
	phone = models.CharField(max_length=15)
	address =  models.CharField(max_length=100)
	city =  models.CharField(max_length=50)
	state =  models.CharField(max_length=50)
	zipcode =  models.CharField(max_length=20)

	def __str__(self):
		return(f"{self.first_name} {self.last_name}")


