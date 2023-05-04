from django.urls import path
from .views import *

urlpatterns = [

    path('ul/', UserListView.as_view(), name='userlist' ),
    path('uc/', UserCreateView.as_view(),name='usercreate' ),
    path('uc/<int:pk>/', UserRUDView.as_view(),name='userRUD' ),

    path('pl/', PostListView.as_view(), name='postlist' ),
    path('pc/', PostCreateView.as_view(), name='postcreate' ),
    path('pc/<int:pk>/', PostRUDView.as_view(), name='postRUD' ),

    path('ll/', LikeListView.as_view(), name='likelist' ),
    path('lc/', LikeCreateView.as_view(), name='likecreate' ),
    path('lc/<int:pk>/', LikeRUDView.as_view(), name='likeRUD' ),
    
]

