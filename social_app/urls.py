from django.urls import path
from .views import(post_lists, post_details,post_edit, 
    post_delete, comment_delete)

urlpatterns = [
    
    path('post_lists', post_lists, name='post_lists'),
    path('post_lists/<int:pk>/', post_details, name='post_details'),
    path('post_lists/<int:pk>/edit/', post_edit, name='post_edit'),
    path('post_lists/<int:pk>/delete/', post_delete, name='post_delete'),
    path('comment/<int:pk>/delete/', comment_delete, name='comment_delete'),
]