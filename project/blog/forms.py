from django import forms
from .models import Post, Comment1

class PostForm1(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content']
'''
	def clean(self):
		cleaned_data = super().clean()
		title = self.cleaned_data['title']
		if len(title) > 20:
			raise forms.ValidationError('Enter less than 20')
		return title
'''

class CommentForm1(forms.ModelForm):
	class Meta:
		model = Comment1
		fields = ['content']