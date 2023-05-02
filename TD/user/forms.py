from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


CHOICES1= [
    ('VFX', 'VFX'),
    ('Roto', 'Roto'),
    ('Paint', 'Paint'),
    ('Supervisor', 'Supervisor'),
    ('Comp','Comp'),
    ('Production','Production'),
    ('Editor','Editor'),
    ('Matchmove','Matchmove'),
    ('MGFX','MGFX'),
    ('DMP','DMP'),
    ('Pipeline','Pipeline'),
    ('IT','IT')
    ]


CHOICES2= [
    ('Intern', 'Intern'),
    ('Artist', 'Artist'),
    ('TD','TD'),
    ('Coordinator', 'Coordinator'),
    ('Team Lead','Team Lead'),
    ('Supervisor','Supervisor'),
    ('HOD','HOD')
    ]


CHOICES3= [
    ('Mr. Riaz patel', 'Mr. Riaz patel'),
    ('Mr. Abhishek', 'Mr. Abhishek'),
    ('Mr. Swapnil', 'Mr. Swapnil'),
    ('Mr. Vinay', 'Mr. Vinay'),
    ('Mr. Kunal', 'Mr. Kunal'),
    ('Mr. Balram', 'Coordinator'),
    ]



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    id1 = forms.IntegerField(label='ID')
    department = forms.CharField(label='Department', widget=forms.Select(choices=CHOICES1))
    designation = forms.CharField(label='Designation', widget=forms.Select(choices=CHOICES2))
    reporting = forms.CharField(label='Reporting', widget=forms.Select(choices=CHOICES3))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'id1', 'department', 'designation', 'reporting']




