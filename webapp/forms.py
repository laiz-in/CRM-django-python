from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import StaffRecords, StudentRecords,ParentRecords 

class SignUpFormForStaff(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control custom-field-bg', 'placeholder':'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control custom-field-bg', 'placeholder':'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control custom-field-bg', 'placeholder':'Last Name'}))
    sno = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control custom-field-bg', 'placeholder':'Sno'}))
    employee_id = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control custom-field-bg', 'placeholder':'Employee ID'}))

    DEPARTMENT_CHOICES = [
        ('Mathematics', 'Mathematics'),
        ('Physics', 'Physics'),
        ('Biology', 'Biology'),
        ('PhysicalEducation', 'PhysicalEducation'),
        ('Chemistry', 'Chemistry'),
        ('Administration', 'Administration'),
        ('English', 'English'),
        ('ComputerScience', 'ComputerScience'),

    ]

    department = forms.ChoiceField(label="", choices=DEPARTMENT_CHOICES, widget=forms.Select(attrs={'class':'form-select custom-field-bg', 'placeholder':'Select Department'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    # Initialize the form
    def __init__(self, *args, **kwargs):
        super(SignUpFormForStaff, self).__init__(*args, **kwargs)

        # Customizing fields in the form
        self.fields['username'].widget.attrs['class'] = 'form-control custom-field-bg'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small></small></span>'
        
        self.fields['password1'].widget.attrs['class'] = 'form-control custom-field-bg'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-light"><li>Your password must contain at least 8 characters.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control custom-field-bg'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small></small></span>'



# Create Add Record Form
class AddStudentRecordForm(forms.ModelForm):
	first_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"First Name", "class":"form-control custom-field-bg"}), label="")
	last_name = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Last Name", "class":"form-control custom-field-bg"}), label="")
	email = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Email", "class":"form-control custom-field-bg"}), label="")
	phone = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Phone", "class":"form-control custom-field-bg"}), label="")
	address = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Address", "class":"form-control custom-field-bg"}), label="")
	city = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"City", "class":"form-control custom-field-bg"}), label="")
	state = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"State", "class":"form-control custom-field-bg"}), label="")
	zipcode = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Zipcode", "class":"form-control custom-field-bg"}), label="")

	class Meta:
		model = StudentRecords
		exclude = ("user",)


# class parentRegistration()