from django import forms
from .models import *
from django.contrib.auth.models import User
from django.utils import timezone


DATE_FORMATS = [ '%Y-%m-%d', ]


CHOICES1= [
    ('Yet To Started', 'Yet To Started'),
    ('In Process', 'In Process'),
    ('Completed', 'Completed'),
    ]


CHOICES2= [
    ('Project1', 'Project1'),
    ('Project2', 'Project2'),
    ('Project3', 'Project3'),
    ('Project4','Project4'),
    ('Project5','Project5'),
    ('Project6','Project6'),
    ]


CHOICES3= [
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


CHOICES4= [
    ('Intern', 'Intern'),
    ('Artist', 'Artist'),
    ('TD','TD'),
    ('Coordinator', 'Coordinator'),
    ('Team Lead','Team Lead'),
    ('Supervisor','Supervisor'),
    ('HOD','HOD')
    ]


CHOICES5= [
    ('Mr. Riaz patel', 'Mr. Riaz patel'),
    ('Mr. Abhishek', 'Mr. Abhishek'),
    ('Mr. Swapnil', 'Mr. Swapnil'),
    ('Mr. Vinay', 'Mr. Vinay'),
    ('Mr. Kunal', 'Mr. Kunal'),
    ('Mr. Balram', 'Coordinator'),
    ]


#####################################################################################################################################


class ShotForm1(forms.ModelForm):
    work_status = forms.CharField(label='Work status', widget=forms.Select(choices=CHOICES1))
    task_assign = forms.CharField(label='Task asign', widget=forms.Select(choices=CHOICES3))
    project_name = forms.CharField(label='Project Name', widget=forms.Select(choices=CHOICES2))
    class Meta:
        model = Shot1
        fields = ['project_name','shot_name','task_assign','work_description','date_started','work_status','date_completed']



class ArtistForm(forms.ModelForm):
    artist_department = forms.CharField(label='Department', widget=forms.Select(choices=CHOICES3))
    artist_designation = forms.CharField(label='Designation', widget=forms.Select(choices=CHOICES4))
    artist_reporting = forms.CharField(label='Reporting', widget=forms.Select(choices=CHOICES5))

    class Meta:
        model = All_Artist
        fields = '__all__'



class ShotFormB(forms.ModelForm):
    work_status = forms.CharField(label='Work status', widget=forms.Select(choices=CHOICES1))
    class Meta:
        model = Shot1
        fields = ['work_status','date_completed']



class UploadFileForm(forms.Form):
    excel_file = forms.FileField()








