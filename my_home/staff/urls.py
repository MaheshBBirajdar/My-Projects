from django.urls import path
from .views import *

urlpatterns =[

	path ('create/', Staff_Create, name='create'),
	path ('read/', Staff_Read, name='view_all'),
	path ('update/<int:id>/', Staff_Update, name='update'),
	path ('delete/<int:id>/', Staff_Delete, name='delete'),

	
]