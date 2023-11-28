from django import forms
from .models import Courses
class DateInput(forms.DateInput):
    input_type = "date"

class AddStudentForm(forms.Form):
    email=forms.EmailField(label=None,max_length=50,widget=forms.EmailInput(attrs={"class":"form-control custom-field-bg mb-2","placeholder": "Enter student email"}))
    password=forms.CharField(label=None,max_length=50,widget=forms.PasswordInput(attrs={"class":"form-control custom-field-bg mb-2","placeholder": "Enter student password"}))
    first_name=forms.CharField(label=None,max_length=50,widget=forms.TextInput(attrs={"class":"form-control custom-field-bg mb-2","placeholder": "Enter student first name"}))
    last_name=forms.CharField(label=None,max_length=50,widget=forms.TextInput(attrs={"class":"form-control custom-field-bg mb-2","placeholder": "Enter student last name"}))
    username=forms.CharField(label=None,max_length=50,widget=forms.TextInput(attrs={"class":"form-control custom-field-bg mb-2","placeholder": "Enter student username"}))
    address=forms.CharField(label=None,max_length=50,widget=forms.TextInput(attrs={"class":"form-control custom-field-bg mb-2","placeholder": "Enter student address"}))

    courses=Courses.objects.all()
    course_list=[]
    for course in courses:
        small_course=(course.id,course.course_name)
        course_list.append(small_course)
    course_list.insert(0, ("", "Select the course"))

    gender_choice=(
        ("", "Select gender"),
        ("Male","Male"),
        ("Female","Female")
    )

    course=forms.ChoiceField(label=None,choices=course_list,widget=forms.Select(attrs={"class":"form-control custom-field-bg mb-2","placeholder": "select the course"}))
    sex=forms.ChoiceField(label=None,choices=gender_choice,widget=forms.Select(attrs={"class":"form-control custom-field-bg mb-2 ","placeholder": "gender"}))
    session_start=forms.DateField(label="Session start ",widget=DateInput(attrs={"class":"form-control mb-2 custom-field-bg w-50  "}))
    session_end=forms.DateField(label="Session end ",widget=DateInput(attrs={"class":"form-control mb-2 custom-field-bg w-50"}))
    profile_pic=forms.FileField(label="Choose profile picture",max_length=50,widget=forms.FileInput(attrs={"class":"form-control w-50 custom-field-bg mb-2","placeholder": "choose the photo"}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
class EditStudentForm(forms.Form):
    email=forms.EmailField(label="Email",max_length=50,widget=forms.EmailInput(attrs={"class":"form-control"}))
    first_name=forms.CharField(label="First Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name=forms.CharField(label="Last Name",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    username=forms.CharField(label="Username",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(label="Address",max_length=50,widget=forms.TextInput(attrs={"class":"form-control"}))

    courses=Courses.objects.all()
    course_list=[]
    for course in courses:
        small_course=(course.id,course.course_name)
        course_list.append(small_course)

    gender_choice=(
        ("Male","Male"),
        ("Female","Female")
    )

    course=forms.ChoiceField(label="Course",choices=course_list,widget=forms.Select(attrs={"class":"form-control"}))
    sex=forms.ChoiceField(label="Sex",choices=gender_choice,widget=forms.Select(attrs={"class":"form-control"}))
    session_start=forms.DateField(label="Session Start",widget=DateInput(attrs={"class":"form-control"}))
    session_end=forms.DateField(label="Session End",widget=DateInput(attrs={"class":"form-control"}))
    profile_pic=forms.FileField(label="Profile Pic",max_length=50,widget=forms.FileInput(attrs={"class":"form-control"}),required=False)
