from django.urls import path
from .import views
from .views import post_lists

urlpatterns = [
    path('', views.post_lists, name='post_list'),
    path('post_lists', post_lists, name='post_lists')
]