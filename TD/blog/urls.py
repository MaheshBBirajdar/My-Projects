from django.urls import path
from .views import *


urlpatterns = [

    path('upload1/', Upload_csv1, name='upload1'),
    path('add_artist1/', Add_Artist1, name='add_artist1'),
    path('all_artist1/', All_Artist1, name='all_artist1'),
    path('add_shot1/', Add_Shot1, name='add_shot1'),
    path('all_shot1/', All_Shot1, name='all_shot1'),
    path('my_shot1/', My_Shot1, name='my_shot1'),
    path('edit_shot1/<int:id>', Edit_Shot1, name='edit_shot1'),
    path('delete_shot1/<int:pk>', Delete_Shot1, name='delete_shot1'),
    path('issueshot1/', IssueShot1, name='issueshot1'),
    path('viewissuedshot1/', ViewIssuedShot1, name='viewissuedshot1'),
    path('delete_issued_shot1/<int:pk>', Delete_Issued_Shot1, name='delete_issued_shot1'),
    path('search/', Search, name='search'),

]
