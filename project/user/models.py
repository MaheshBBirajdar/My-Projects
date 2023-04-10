from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
	
	user = models.OneToOneField(User,related_name="profile", on_delete= models.CASCADE)
	age = models.IntegerField(null=True)
	image = models.ImageField(default='default.jpg', upload_to='profile_pic')