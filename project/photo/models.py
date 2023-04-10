from django.db import models

class PhotoGal(models.Model):
	multipleimg = models.FileField(upload_to='Gallery', blank=True, null=True)
