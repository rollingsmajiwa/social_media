from django.urls import path
from .views import post_lists, post_details

urlpatterns = [
    
    path('post_lists', post_lists, name='post_lists'),
    path('post_lists/<int:pk>/', post_details, name='post_details')
]