from django import forms

class StudentForm(forms.Form):
	uid = forms.IntegerField(label= 'UID')
	name = forms.CharField(max_length=100, label='NAME')
	mail = forms.EmailField(max_length=100, label='MAIL')
	sclass = forms.CharField(max_length=100, label='CLASS')



class PythonDjangoForm(forms.Form):
	rollnum = forms.IntegerField(label='ROLL_NO')
	subject = forms.CharField(max_length=100, label='SUBJECT')
	marks = forms.CharField(max_length=100, label='GRADE')