from django.urls import path
from .views import *


urlpatterns = [

    path('upload1/', Import_Excel, name='upload1'),
    path('add_shot1/', Add_Shot1, name='add_shot1'),
    path('all_shot1/', All_Shot1, name='all_shot1'),
    path('my_shot1/', My_Shot1, name='my_shot1'),
    path ('add/', AddArtist, name='addartist'),
    path ('all/', AllArtist, name='allartist'),
    path('edit_shot1/<int:id>', Edit_Shot1, name='edit_shot1'),
    path('delete_shot1/<int:pk>', Delete_Shot1, name='delete_shot1'),
    path('search/', Search, name='search'),

]
