from django.urls import path
from .views import *


urlpatterns = [

		path ('pic/', multiple_upload, name="pic"),
]