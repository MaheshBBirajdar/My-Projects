from django.urls import path
from .views import *

urlpatterns = [
    
    path('',Home, name='home_page'),
    path('signup/', User_Signup, name='sign_up'),
    path('login/', User_Signin, name='sign_in'),
    path('logout/', User_Signout, name='sign_out'),
]
