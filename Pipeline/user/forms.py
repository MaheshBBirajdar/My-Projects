from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.core.exceptions import ValidationError
from django.utils import timezone


CHOICES1= [
    ('Roto', 'Roto'),
    ('Paint', 'Paint'),
    ('Comp','Comp'),
    ('CG','CG'),
    ('Production','Production'),
    ('Editor','Editor'),
    ('Matchmove','Matchmove'),
    ('MGFX','MGFX'),
    ('DMP','DMP'),
    ('Pipeline','Pipeline'),
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
    ('DONE', 'DONE'),
    ]


CHOICES5= [
    ('Project1', 'Project1'),
    ('Project2', 'Project2'),
    ('Project3', 'Project3'),
    ('Project4','Project4'),
    ('Project5','Project5'),
    ('Project6','Project6'),
    ]

##################################################################################################################################

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    uid = forms.IntegerField(label='UID')
    department = forms.CharField(label='Department', widget=forms.Select(choices=CHOICES1))
    designation = forms.CharField(label='Designation', widget=forms.Select(choices=CHOICES2))
    reporting = forms.CharField(label='Reporting', widget=forms.Select(choices=CHOICES3))

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('email','uid', 'department','designation','reporting')


###################################################################################################################################

class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']

###################################################################################################################################


class StudentSigupForm(forms.ModelForm):
    email = forms.EmailField(label='Email [@osvfx.com]')
    class Meta:
        model = User
        fields= ['first_name','last_name','email','username', 'password']


####################################################################################################################################

class StudentExtraForm(forms.ModelForm):
    aid = forms.IntegerField(label='Emp ID')
    class Meta:
        model = StudentExtra
        fields = ['aid','department','designation', 'reporting']

####################################################################################################################################

class CustomDateInput(forms.DateInput):
    input_type = 'date'
    format = '%d/%m/%Y'

class ShotForm(forms.ModelForm):
    dependency = forms.ModelMultipleChoiceField(queryset=StudentExtra.objects.all(), required=False, widget=forms.CheckboxSelectMultiple, label='Dependencies')
    eta = forms.DateField(label='TGT Date', widget=CustomDateInput)
    class Meta:
        model=Shot2
        fields = ['project_name','shot_name','work_description','date_started','eta','work_status','dependency']

#####################################################################################################################################

class EditShotForm(forms.ModelForm):
    project_name = forms.ModelChoiceField(queryset = Shot2.objects.values_list('project_name', flat=True).distinct(),to_field_name="project_name",label='Project Name')
    dependency = forms.ModelMultipleChoiceField(queryset=StudentExtra.objects.all(), required=False, widget=forms.CheckboxSelectMultiple, label='Dependencies')

    class Meta:
        model = Shot2
        fields = ['project_name','shot_name','work_description','eta','dependency']
                    
######################################################################################################################################

class CustomDateInput(forms.DateInput):
    input_type = 'date'
    format = '%d/%m/%Y'


class IssuedShotForm(forms.Form):
    department1 = forms.ModelChoiceField(queryset = StudentExtra.objects.all(),to_field_name='department',label='Artist & Department')
    projectname1 = forms.ModelChoiceField(queryset = Shot2.objects.values_list('project_name', flat=True).distinct(),to_field_name="project_name",label='Project Name')
    shotname1 = forms.CharField(label='Shot Name')
    eta1 = forms.DateField(label='TGT Date', widget=CustomDateInput)
    note1 = forms.CharField(label='Note')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department1'].label_from_instance = self.label_from_department_instance


    def label_from_department_instance(self, obj):
        return obj.user.first_name + ' [' + str(obj.department) + ']'
    
    
    def clean_eta1(self):
        eta_date = self.cleaned_data['eta1']
        current_date = timezone.now().date()
        if eta_date <= current_date:
            raise ValidationError("TGT date must be greater than the today.")
        return eta_date


    def clean(self):
        cleaned_data = super().clean()
        department = cleaned_data.get('department1')
        project_name = cleaned_data.get('projectname1')
        shot_name = cleaned_data.get('shotname1')

        if department and project_name and shot_name:
            existing_shots = IssuedShot.objects.filter(
                department=department,
                project_name=project_name,
                shot_name=shot_name)
            if existing_shots.exists():
                raise ValidationError("This shot has already been issued to the same artist.")


    def clean_shotname1(self):
        project_name = self.cleaned_data['projectname1']
        shot_name = self.cleaned_data['shotname1']
        if not Shot2.objects.filter(project_name=project_name, shot_name=shot_name).exists():
            raise ValidationError("This shot name is not available in the selected project.")
        return shot_name

######################################################################################################################################

class SendFeedbackForm(forms.ModelForm):
    project_name = forms.ModelChoiceField(queryset = Shot2.objects.values_list('project_name', flat=True).distinct(),to_field_name="project_name",label='Project Name')
    department = forms.ModelChoiceField(queryset = StudentExtra.objects.values_list('department', flat=True).distinct(),to_field_name="department",label='Department')
    
    class Meta:
        model = SendFeedback
        fields = ['department','project_name','shot_name','work_status','content','date_posted']

######################################################################################################################################

class EditFeedbackForm(forms.ModelForm):
    class Meta:
        model = SendFeedback
        fields = ['work_status','content']

###################################################################################################################################

class ReIssuedShotForm(forms.Form):
    department1 = forms.ModelChoiceField(queryset = StudentExtra.objects.all(),to_field_name='department',label='Artist & Department')
    projectname1 = forms.ModelChoiceField(queryset = Shot2.objects.values_list('project_name', flat=True).distinct(),to_field_name="project_name",label='Project Name')
    shotname1 = forms.CharField(label='Shot Name')
    eta1 = forms.DateField(label='TGT Date', widget=CustomDateInput)
    note1 = forms.CharField(label='Note')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department1'].label_from_instance = self.label_from_department_instance


    def label_from_department_instance(self, obj):
        return obj.user.first_name + ' [' + str(obj.department) + ']'
    
    
    def clean_eta1(self):
        eta_date = self.cleaned_data['eta1']
        current_date = timezone.now().date()
        if eta_date <= current_date:
            raise ValidationError("TGT date must be greater than the today.")
        return eta_date


    def clean_shotname1(self):
        project_name = self.cleaned_data['projectname1']
        shot_name = self.cleaned_data['shotname1']
        if not Shot2.objects.filter(project_name=project_name, shot_name=shot_name).exists():
            raise ValidationError("This shot name is not available in the selected project.")
        return shot_name