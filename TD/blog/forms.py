from django import forms
from .models import *
from django.contrib.auth.models import User
from django.utils import timezone


DATE_FORMATS = [ '%Y-%m-%d', ]


CHOICES1= [
    ('Yet Not Started', 'Yet Not Started'),
    ('In Process', 'In Process'),
    ('Completed', 'Completed'),
    ]


CHOICES2= [
    ('Roto', 'Roto'),
    ('Paint', 'Paint'),
    ('Supervisor', 'Supervisor'),
    ('Comp','Comp'),
    ('Production','Production'),
    ('Editor','Editor'),
    ('Matchmove','Matchmove'),
    ('MGFX','MGFX'),
    ('Pipeline','Pipeline')
    ]


CHOICES3= [
    ('Project1', 'Project1'),
    ('Project2', 'Project2'),
    ('Project3', 'Project3'),
    ('Project4','Project4'),
    ('Project5','Project5'),
    ('Project6','Project6'),
    ]




#####################################################################################################################################

class ArtistForm1(forms.ModelForm):
    class Meta:
        model = Artist1
        fields = ['artist','shot','a_id1','department','designation','reporting']


class ShotForm1(forms.ModelForm):
    work_status = forms.CharField(label='Work status', widget=forms.Select(choices=CHOICES1))
    task_assign = forms.CharField(label='Task asign', widget=forms.Select(choices=CHOICES2))
    project_name = forms.CharField(label='Project Name', widget=forms.Select(choices=CHOICES3))
    class Meta:
        model = Shot1
        fields = ['project_name','shot_number','task_assign','work_description','date_started','work_status','date_completed']



class ShotFormB(forms.ModelForm):
    work_status = forms.CharField(label='Work status', widget=forms.Select(choices=CHOICES1))
    class Meta:
        model = Shot1
        fields = ['work_status','date_completed']



class IssuedShotForm1(forms.Form):
    projectname = forms.ModelChoiceField(queryset=Shot1.objects.all(), to_field_name="project_name",label='Project Name')



class UploadFileForm(forms.Form):
    file = forms.FileField()



class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100)

