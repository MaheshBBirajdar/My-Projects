from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=200)
	content = models.TextField()
	date1 = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User,related_name='post', on_delete=models.CASCADE)

	def __str__(self):
		return self.title	

	def get_absolute_url(self):                                    ### Class based View
		print('pk  is -->', self.pk, type(self))
		return reverse('cls-detail', kwargs={'pk':self.pk})



class Comment1(models.Model):
	post = models.ForeignKey(Post, related_name='comment_post', on_delete=models.CASCADE)
	content = models.TextField()
	create_date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User, related_name='comment_user', on_delete=models.CASCADE)
	approved_comment = models.BooleanField(default=False)

	def __str__(self):
		return self.content

	def approve(self):
		self.approve_comment = True
		self.save()