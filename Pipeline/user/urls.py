from django.urls import path
from .views import *

urlpatterns = [
    
#    path ('', home, name='homepage'),
    path ('register/',register, name='register'),
    path ('login/',Login, name='login'),
    path ('logout/',Logout, name='logout'),


    path('', home_view,name='h'),

    path('adminclick/', adminclick_view, name='adminclick'),
    path('studentclick/', studentclick_view, name='studentclick'),

    path('adminsignup', adminsignup_view, name='adminsignup'),
    path('studentsignup', studentsignup_view, name='studentsignup'),

    path('afterlogin', afterlogin_view, name='afterlogin'),

    path('allartist/', allartist_view, name='allartist1'),

    path('editartist/<int:id>/', editartist_view ,name='editartist'),

    path('deleteartist/<int:pk>/', deleteartist_view ,name='deleteartist'),

    path('importdata/', import_excel, name='importdata'),

    path('addshot/', addshot_view, name='addshot'),

    path('allshot/', allshot_view, name='allshot'),

    path('allshot1/', allshot_view1, name='mang_message1'),

    path('allproject/', allproject_view, name='allproject'),                                            # All Projects

    path('project_shots/<str:project_name>/', project_shots_view, name='pshots'),                       # Shot by project wise

    path('editshot/<int:id>/', editshot_view ,name='editshot'),

    path('deleteshot/<int:pk>/', deleteshot_view ,name='deleteshot'),
            
    path('search/', searchshot_view, name= 'search'),

    path('search1/', searchprojectshot_view, name= 'search1'),

    path('search2/', search_issuedshots_view, name= 'search2'),

    path('search3/', searchshot_mang_view, name= 'search3'),

    path('issueshot/', issueshot_view, name='issueshot'),

    path('viewissuedshot/', viewissuedshot_view, name='viewissuedshot'),

    path('deleteissuedshot/<int:pk>/', deleteissuedshot_view, name='deleteissuedshot'),
    
    path('viewissuedshotbyartist/', viewissuedshotbyartist_view, name='viewissuedshotbyartist'),

    path('sendfeedback/', sendfeedback_view, name='sendfeedback'),

    path('allfeedback/', allfeedback_view, name='allfeedback'),

    path('deletefeedback/<int:pk>/', deletefeedback_view, name='deletefeedback'),

    path('myfeedback/', myfeedback_view, name='myfeedback'),

    path('artist-portal/', artist_portal, name='popup_message'),                                            # popup message

    path('mang-portal/', management_portal, name='popup_mang_message'),

    path('reviewed-shot/<int:shot_id>/', reviewed_shot, name='reviewed_shot'),

    path('reissueshot/', re_issueshot_view, name='re_issueshot'),
    
    path('delete_mang_message_view/<int:pk>/', delete_mang_message_view, name='delete'),        

    path('final_approve_shot/<int:pk>/', final_approved_shot, name='final_approved_shot'),      
]