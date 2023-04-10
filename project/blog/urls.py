from django.urls import path
from .views import *



urlpatterns = [
   
# Function Based    
    path('createpost/', CreatePost1, name='fun-createpost'),
    path('allpost/', Allpost1, name='fun-allpost'),
    path('allpost/<int:id1>', Specificpost1, name='fun-specific_post'),
    path('pages/<int:page>', Allpost1, name='pages'),
    path('clsview/<int:id1>', CommentPost1, name='fun-post-comment'),
    path('clsview/<int:id1>/approve/', comment_approve, name='fun-post-approve'),

# Class Based
    path('clspost/', PostCreateView1.as_view(), name='cls-createpost'),
    path('clsview/', PostListView1.as_view(), name='cls-view'),
    path('clsview/<int:pk>', PostDetailView1.as_view(), name='cls-detail'),
    path('clsview/mypost/', UserPostListView1.as_view(), name='cls-user-view'),
    path('clsview/otherpost/<str:u1>', OtherUserPostListView1.as_view(), name='cls-other-user-view'),
    path('clsview/<int:pk>/update/', PostUpdateView1.as_view(), name='cls-post-update'),
    path('clsview/<int:pk>/delete/', PostDeleteView1.as_view(), name='cls-post-delete'),
    
]