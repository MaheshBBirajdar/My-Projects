from django.urls import path
from .views import *


urlpatterns = [
    
    path('',hello),
    path('hi/',hi),
    path('ok/',ok),
    path('html/',html),
    path('heros/', holly),
    path('form/', Student1, name='form'),
    path('pyd/', PyD, name='python'),
    path('pd/', pd, name='pd'),
]
