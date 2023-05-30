from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *



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


CHOICES4= [
    ('YTS', 'YTS'),
    ('WIP', 'WIP'),
    ('Completed', 'Completed'),
    ]


CHOICES5= [
    ('Project1', 'Project1'),
    ('Project2', 'Project2'),
    ('Project3', 'Project3'),
    ('Project4','Project4'),
    ('Project5','Project5'),
    ('Project6','Project6'),
    ]



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    uid = forms.IntegerField(label='UID')
    department = forms.CharField(label='Department', widget=forms.Select(choices=CHOICES1))
    designation = forms.CharField(label='Designation', widget=forms.Select(choices=CHOICES2))
    reporting = forms.CharField(label='Reporting', widget=forms.Select(choices=CHOICES3))

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email','uid', 'department','designation','reporting')




class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']




class StudentSigupForm(forms.ModelForm):
    email = forms.EmailField(label='Email')
    class Meta:
        model=User
        fields= ['first_name','last_name','email','username', 'password']




class StudentExtraForm(forms.ModelForm):
    class Meta:
        model = StudentExtra
        fields = ['aid','department','designation', 'reporting']




class ShotForm(forms.ModelForm):
    class Meta:
        model=Shot2
        fields = ['project_name','shot_name','work_description','date_started','work_status','eta']




class EditShotForm(forms.ModelForm):
    class Meta:
        model = Shot2
        fields = ['work_status','eta']
                    



class IssuedShotForm(forms.Form):
    projectname1 = forms.ModelChoiceField(queryset = Shot2.objects.values_list('project_name', flat=True).distinct(),to_field_name="project_name",label='Project Name')
    shotname1 = forms.ModelChoiceField(queryset = Shot2.objects.values_list('shot_name', flat=True).distinct(),to_field_name="shot_name",label='Shot Name')
    department1 = forms.ModelChoiceField(queryset = StudentExtra.objects.all(),to_field_name='department',label='Artist')
   
    
    

class SendFeedbackForm(forms.ModelForm):
    project_name = forms.ModelChoiceField(queryset = Shot2.objects.values_list('project_name', flat=True).distinct(),to_field_name="project_name",label='Project Name')
    shot_name = forms.ModelChoiceField(queryset = Shot2.objects.values_list('shot_name', flat=True).distinct(),to_field_name="shot_name",label='Shot Name')
    department = forms.ModelChoiceField(queryset = StudentExtra.objects.values_list('department', flat=True).distinct(),to_field_name="department",label='Department')

    class Meta:
        model = SendFeedback
        fields = ['department','project_name','shot_name','status','content','date_posted']