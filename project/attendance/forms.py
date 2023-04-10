from .models import Studentdata2, Mark_attendance2
from django import forms

class StudentForm(forms.ModelForm):
	class Meta:
		model = Studentdata2
		fields = ['stuid', 'stuname', 'stumail']

class StudentMarkForm(forms.ModelForm):
	class Meta:
		model = Mark_attendance2
		fields = ['uid','subject_name']

class StudentMarkFormDisplay(forms.Form):
	uid = forms.IntegerField(label= 'UID')