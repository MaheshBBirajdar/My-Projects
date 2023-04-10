"""batch4 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_view
from user import views as user_view
#from user import views as user_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',include('base.urls')),
    path('attendance/', include('attendance.urls')),
    path('user/', include('user.urls')),
    path('', user_view.Loginpage),
    path('login/', user_view.Loginpage),
    
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='user/pass_reset.html'), name='password-reset'),

    path('password_reset_confirm/<uidb64>/<token>',
        auth_view.PasswordResetConfirmView.as_view(template_name='user/pass_reset_cnfm.html'), name='password_reset_confirm'),

    path('password_reset_done/', 
        auth_view.PasswordResetDoneView.as_view(template_name='user/pass_reset_done.html'),name='password_reset_done'),

    path('password_reset_complete/', 
        auth_view.PasswordResetCompleteView.as_view(template_name='user/pass_reset_complete.html'),name='password_reset_complete'),

    path('blog/', include('blog.urls')),
    path('photo/', include('photo.urls')),
    path('api-auth/', include('rest_framework.urls')),

]


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)