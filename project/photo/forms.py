from django import forms
from .models import PhotoGal

class PicForm(forms.ModelForm):
	class Meta:
		model = PhotoGal
		fields = ['multipleimg']
		widgets = {'multipleimg':forms.FileInput(attrs={'id':'myfile','class':'form-control-file','multiple':True})} 
