from django.db import models


class Staff(models.Model):
	Ename = models.CharField(max_length=100)
	Elastname = models.CharField(max_length=100)
	Email = models.EmailField()
	Edepart = models.CharField(max_length=100)
	Edesg = models.CharField(max_length=100) 
	Epay = models.IntegerField()
	

	def __str__(self):
		return self.Ename