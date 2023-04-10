from django.db import models

# Create your models here.
class Studentdata(models.Model):
	class Meta:
		unique_together = (('stuid','subject'))
	stuid = models.IntegerField()
	stuname = models.CharField(max_length=100)
	stumail = models.EmailField(max_length=100)
	subject = models.CharField(max_length=100)

	def __str__(self):
		return str(self.stuid)


class Studentdata1(models.Model):
	class Meta:
		unique_together = (('stuid','subject'))
	stuid = models.IntegerField()
	stuid_sub = models.CharField(unique=True, max_length=100)
	stuname = models.CharField(max_length=100)
	stumail = models.EmailField(max_length=100)
	subject = models.CharField(max_length=100)

	def __str__(self):
		return str(self.stuid)


class Mark_attendance(models.Model):
	class Meta:
		unique_together = (('uid','date1'),('ip_address','date1'))
	uid = models.ForeignKey('Studentdata1', related_name='uid', to_field='stuid_sub', on_delete= models.CASCADE)
	time1 = models.IntegerField(null=False)
	date1 = models.CharField(max_length=100, null=False)
	subject_name = models.CharField(max_length=100, null=False)
	ip_address = models.CharField(max_length=100, null=False)
	platform = models.CharField(max_length=200, null=False) 

	def __str__(self):
		return str(self.id)


class Studentdata2(models.Model):
	stuid = models.IntegerField(unique=True, null=False)
	stuname = models.CharField(max_length=100)
	stumail = models.EmailField(max_length=100)
	
	def __str__(self):
		return str(self.stuid)


class Mark_attendance2(models.Model):
	class Meta:
		unique_together = (('uid','date1'),('ip_address','date1'))
	uid = models.ForeignKey('Studentdata2', related_name='uid', to_field='stuid', on_delete= models.CASCADE)
	time1 = models.IntegerField(null=False)
	date1 = models.CharField(max_length=100, null=False)
	subject_name = models.CharField(max_length=100, null=False)
	ip_address = models.CharField(max_length=100, null=False)
	platform = models.CharField(max_length=200, null=False) 

	def __str__(self):
		return str(self.id)


class Laptop(models.Model):
	lap_id = models.IntegerField()
	lap_name = models.CharField(max_length=100)
	lap_model = models.CharField(max_length=100)

	def __str__(self):
		return str(self.lap_id)
