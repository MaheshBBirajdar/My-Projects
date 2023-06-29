from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.exceptions import ValidationError
from datetime import datetime,timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models




CHOICES1= [
    ('VFX', 'VFX'),
    ('Roto', 'Roto'),
    ('Paint', 'Paint'),
    ('CG', 'CG'),
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
    ('Data IO','Data IO'),
    ('Jr. Artist', 'Jr. Artist'),
    ('Sr. Artist', 'Sr. Artist'),
    ('Pipeline TD','Pipeline TD'),
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
    ('Mr. Vinay Kadam', 'Mr. Vinay Kadam'),
    ('Mr. Kunal Salunkhe', 'Mr. Kunal Salunkhe'),
    ('Ms. Ankita Goyal', 'Ms. Ankita Goyal'),
    ('Mr. Bhushan Pawar', 'Mr. Bhushan Pawar'),
    ]


CHOICES4= [
    ('YTS', 'YTS'),
    ('WIP', 'WIP'),
    ('DONE', 'DONE'),
    ]


CHOICES5= [
    ('TEJAS', 'TEJAS'),
    ('BNG', 'BNG'),
    ('JAWAN', 'JAWAN'),
    ('SOUP', 'SOUP'),
    ('ADIPURUSH', 'ADIPURUSH'),
    ('IC', 'IC'),
    ]



###############################################################################################################################################

class Shot2(models.Model):
    dependency = models.ManyToManyField('StudentExtra',verbose_name='Dependencies')
    project_name = models.CharField(max_length=25, verbose_name='Project Name')
    shot_name = models.CharField(max_length=25, verbose_name='Shot Name')
    work_description = models.CharField(max_length=200, verbose_name='Scope of Work')
    date_started = models.DateTimeField(default=timezone.now, verbose_name='Date Posted')
    work_status = models.CharField(max_length=100,choices=CHOICES4, verbose_name='Shot Status')
    eta = models.DateField(null=True, blank=True,default=None, verbose_name='TGT Date (y-m-d)')                              # YYYY-MM-DD
    
    def __str__(self):
        return self.project_name 
    
    
    def clean(self):                                          
        existing_shots = Shot2.objects.filter(
                    project_name=self.project_name,
                    shot_name=self.shot_name
                    ).exclude(id=self.id)  

        if existing_shots.exists():
            raise ValidationError("This shot has already been added in the system.")


    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


    def save(self, *args, **kwargs):
        is_new_shot = self._state.adding
        super().save(*args, **kwargs)
        if is_new_shot:
            message = f"A new shot '{self.shot_name}' has been added to the project '{self.project_name}' ."
            ArtistMessage.objects.create(shot=self, message=message)


        if self.work_status == 'REVIEWED':
            message = f"The shot '{self.shot_name}' in the project '{self.project_name}' has been reviewed."
            ManagementMessage.objects.create(shot=self, message=message)

####################################################################################################################################################   
   

class StudentExtra(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    aid = models.IntegerField(unique=True)
    department = models.CharField(max_length=40, choices=CHOICES1)
    designation = models.CharField(max_length=40, choices=CHOICES2)
    reporting = models.CharField(max_length=40, choices=CHOICES3)

    def __str__(self):
        return self.user.first_name + ' ' + '[' + str(self.department) + ']'
    
    
    def __str__(self):
        return str(self.department) 
    
    
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


#######################################################################################################################################################

def get_expiry():
    return datetime.today() + timedelta(days=2)


class IssuedShot(models.Model):
    work_status = models.CharField(max_length=100, choices=CHOICES4, verbose_name='Shot Status')
    department = models.CharField(max_length=40)
    project_name = models.CharField(max_length=100)
    shot_name = models.CharField(max_length=100)
    issuedate = models.DateField(auto_now=True)
    eta = models.DateField(null=True, blank=True, default=None)
    note = models.CharField(max_length=200, null=True, blank=True, default=None)

    def __str__(self):
        return  self.project_name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

'''
    def clean(self):
        existing_shots = IssuedShot.objects.filter(
            department=self.department,
            project_name=self.project_name,
            shot_name=self.shot_name).exclude(pk=self.pk) 

        if existing_shots.exists():
            raise ValidationError("This shot has already been issued to the same artist.")
        
        if not Shot2.objects.filter(shot_name=self.shot_name).exists():
            raise ValidationError("This shot does not exist.")

        if not Shot2.objects.filter(project_name=self.project_name, shot_name=self.shot_name).exists():
            raise ValidationError("This shot name is not available in the selected project.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
'''

#########################################################################################################################################################


class SendFeedback(models.Model):
    sender1 = models.ForeignKey(User,on_delete=models.CASCADE)
    project_name = models.CharField(max_length=25)
    shot_name = models.CharField(max_length=25)
    content = models.TextField(max_length=100)
    work_status = models.CharField(max_length=25, choices = CHOICES4)
    date_posted = models.DateTimeField(default=timezone.now)
    department = models.CharField(max_length=100)
    issued_shot = models.ForeignKey(IssuedShot, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.work_status
    
    def clean(self):
        super().clean()
        try:
            Shot2.objects.get(project_name=self.project_name, shot_name=self.shot_name)
        except Shot2.DoesNotExist:
            raise ValidationError("Invalid shot name.")


@receiver(post_save, sender=SendFeedback)
def update_shot2_work_status(sender, instance, **kwargs):
    if instance.issued_shot:
        IssuedShot.objects.filter(
            department=instance.issued_shot.department,
            project_name=instance.issued_shot.project_name,
            shot_name=instance.issued_shot.shot_name
        ).update(work_status=instance.work_status)


#########################################################################################################################################################

class ArtistMessage(models.Model):                                                       # send popup message to artist portal 
    shot = models.ForeignKey(Shot2, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    date_sent = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message

###########################################################################################################################################################

class ManagementMessage(models.Model):                                                       # send popup message to artist portal 
    shot = models.ForeignKey(Shot2, on_delete=models.CASCADE)
    message = models.CharField(max_length=200)
    date_sent = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message