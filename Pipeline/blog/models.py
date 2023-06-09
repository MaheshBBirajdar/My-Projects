from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

####################################################################################################################################

class Shot1(models.Model):
    supervisor = models.ForeignKey(User,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    shot_name = models.CharField(max_length=50)
    task_assign = models.CharField(max_length=100)
    work_description = models.CharField(max_length=200)
    date_started = models.DateTimeField(default=timezone.now)
    work_status = models.CharField(max_length=100)
    date_completed = models.DateField(null=True, blank=True)
   
    def __str__(self):
        return self.project_name



class All_Artist(models.Model):
    artist_name = models.CharField(max_length=50)
    artist_id = models.IntegerField(unique=True)
    artist_mail = models.EmailField()
    artist_department = models.CharField(max_length =50)
    artist_designation = models.CharField(max_length=50)
    artist_reporting = models.CharField(max_length=50)

    def __str__(self):
        return self.artist_name


