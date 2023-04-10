from django.urls import path
from.views import *

urlpatterns = [
    
    path('reg/', StudentMasterForm, name='Regform'),
    path('mark/', Mark_Student, name='mark'),
    path('display/',display_attendance, name='display'),
    path('displayone/',One_attendance, name='display-one'),

    # Function Based API
    path('stuinfo/<int:pk>', Studetails, name='api-stu'),
    path('student_api/', student_api),
    
    # Class Based API
    path('list_api/', StudentListAPIView.as_view(), name='student_listapiview'),
    path('create_api/', StudentCreateAPIView.as_view(), name='student_createapiview'),
    path('create_api/<int:pk>', StudentRetrieveAPIView.as_view(), name='student_retrieveapiview'),
    path('update_api/<int:pk>', StudentUpdateAPIView.as_view(), name='student_updateapiview'),
    path('delete_api/<int:pk>', StudentDestroyAPIView.as_view(), name='student_destroyapiview'),
    path('list_create_api/', StudentListCreateAPIView.as_view(), name='student_listcreateapiview'),
    path('create_update_api/<int:pk>', StudentRetrieveUpdateAPIView.as_view(), name='student_retrieveupdateapiview'),
    path('create_retdes_api/<int:pk>', StudentRetrieveDestroyAPIView.as_view(), name='student_retrievedestroyapiview'),
    path('create_retupdes_api/<int:pk>', StudentRetrieveUpdateDestroyAPIView.as_view(), name='student_retrieveupdatedestroyapiview'),

    
]
