from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



CHOICES1= [
    ('VFX', 'VFX'),
    ('Roto', 'Roto'),
    ('Paint', 'Paint'),
    ('Supervisor', 'Supervisor'),
    ('Comp','Comp'),
    ('Production','Production'),
    ('Editor','Editor'),
    ('Matchmove','Matchmove'),
    ('MGFX','MGFX'),
    ('DMP','DMP'),
    ('Pipeline','Pipeline'),
    ('IT','IT')
    ]


CHOICES2= [
    ('Intern', 'Intern'),
    ('Trainee', 'Trainee'),
    ('Jr. Artist', 'Jr. Artist'),
    ('Sr. Artist', 'Sr. Artist'),
    ('TD','TD'),
    ('Coordinator', 'Coordinator'),
    ('Team Lead','Team Lead'),
    ('Supervisor','Supervisor'),
    ('Manager','Manager'),
    ('HOD','HOD')
    ]


CHOICES3= [
    ('Mr. Riaz patel', 'Mr. Riaz patel'),
    ('Mr. Abhishek Kulkarni', 'Mr. Abhishek Kulkarni'),
    ('Mr. Swapnil Kharche', 'Mr. Swapnil Kharche'),
    ('Mr. Vinay', 'Mr. Vinay'),
    ]


CHOICES4= [
    ('YTS', 'YTS'),
    ('WIP', 'WIP'),
    ('Done', 'Done'),
    ]


CHOICES5= [
    ('Tejas', 'Tejas'),
    ('BNG', 'BNG'),
    ('Jawan', 'Jawan'),
    ('Soup','Soup'),
    ]


CHOICES6 = [
    ('WIP', 'WIP'),
    ('Done', 'Done'),
    ]



class Shot2(models.Model):
    project_name = models.CharField(max_length=100, choices=CHOICES5)
    shot_name = models.CharField(max_length=100)
    task_assign = models.CharField(max_length=100, choices=CHOICES1)
    work_description = models.CharField(max_length=200)
    date_started = models.DateTimeField(default=timezone.now)
    work_status = models.CharField(max_length=100, choices=CHOICES4)
    eta = models.DateField(null=True, blank=True,default=None)                              # YYYY-MM-DD
    
    def __str__(self):
        return self.project_name 
    
    
    

class StudentExtra(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    aid = models.IntegerField(unique=True)
    department = models.CharField(max_length=40, choices=CHOICES1)
    designation = models.CharField(max_length=40, choices=CHOICES2)
    reporting = models.CharField(max_length=40, choices=CHOICES3)

    def __str__(self):
        return self.user.first_name + ' ' + '[' + str(self.department) + ']'
    
    @property
    def get_name(self):
        return self.user.first_name + ' ' + self.user.last_name
    
    @property
    def getuserid(self):
        return self.user.aid

    @property
    def get_department_name(self):
        if self.department:
            return self.department.department
        return None




class IssuedShot(models.Model):
    department = models.CharField(max_length=40)
    project_name = models.CharField(max_length=100)
    shot_name = models.CharField(max_length=100)
    issuedate = models.DateField(auto_now=True)

    def __str__(self):
        return  self.department
    




class SendFeedback(models.Model):
    sender = models.ForeignKey(User,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=100)
    shot_name = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    status = models.CharField(max_length=100, choices = CHOICES6)
    date_posted = models.DateTimeField(default=timezone.now)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.status

    