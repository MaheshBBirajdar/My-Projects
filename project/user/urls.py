from django.urls import path
from .views import *
from django.contrib.auth import views as auth_view


urlpatterns = [
    
    path('register/', Register, name='register'),
    #path('login/', auth_view.LoginView.as_view(template_name='user/disform.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    path('profile/',Profile, name='profile'),
    path('login/', Loginpage, name='login'),
    path('profile/<int:id1>',Profile_user, name='profile_user'),
    path('update/',UpdateProfile1, name='upprofile'),
    path('updatepass/',user_change_pass, name='updatepass'),
    
]