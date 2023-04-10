from django.contrib import admin
from .models import Studentdata

@admin.register(Studentdata)
class StudentAdmin(admin.ModelAdmin):
	list_display = ['stuid', 'stuname', 'stumail', 'subject']


# Register your models here.
