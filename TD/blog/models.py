from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from datetime import timedelta




class Shot(models.Model):
    artist = models.ForeignKey(User,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    task_assign = models.CharField(max_length=100)
    work_description = models.CharField(max_length=200)
    date_started = models.DateTimeField(default=timezone.now)
    work_status = models.CharField(max_length=100)
    date_completed = models.DateField()
   
    def __str__(self):
        return self.project_name




class Artist(models.Model):
    artist_id = models.IntegerField(unique=True)
    fullname = models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    department = models.CharField(max_length=100)
    reporting_person = models.CharField(max_length=100)
 
    def __str__(self):
        return self.fullname




def get_expiry(): 
    return datetime.date.today() + timedelta(days=15)


class IssuedShot(models.Model):
    taskassign=models.CharField(max_length=30)
    projectname=models.CharField(max_length=30)
    issuedate=models.DateField(auto_now=True)
    expirydate=models.DateField(default=get_expiry)
    def __str__(self):
        return self.taskassign

####################################################################################################################################



class Shot1(models.Model):
    supervisor = models.ForeignKey(User,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    shot_number = models.IntegerField()
    task_assign = models.CharField(max_length=100)
    work_description = models.CharField(max_length=200)
    date_started = models.DateTimeField(default=timezone.now)
    work_status = models.CharField(max_length=100)
    date_completed = models.DateField(null=True, blank=True)
   
    def __str__(self):
        return self.project_name




class Artist1(models.Model):
    artist = models.ForeignKey(User,on_delete=models.CASCADE)
    shot = models.ForeignKey(Shot1,on_delete=models.CASCADE)
    a_id1 = models.IntegerField()
    department = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    reporting = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.artist)
    
    

class IssuedShot1(models.Model):
    projectname = models.CharField(max_length=100)

    def __str__(self):
        return self.projectname