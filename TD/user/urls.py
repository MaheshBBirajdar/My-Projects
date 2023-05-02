from django.urls import path
from .views import *

urlpatterns = [
    
    path ('', home, name='homepage'),
    path ('register/',register, name='register'),
    path ('login/',Login, name='login'),
    path ('logout/',Logout, name='logout'),
]