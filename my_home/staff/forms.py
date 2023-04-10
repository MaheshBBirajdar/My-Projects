from django import forms
from .models import *


class Staff_Form(forms.ModelForm):
	class Meta:
		model = Staff
		fields = ['Ename','Elastname','Email','Edepart','Edesg','Epay']

