from django.urls import path
from . import views

urlpatterns = [
    # Template View Routes
    path('', views.post_lists, name='post_lists'),
    path('post_lists/', views.post_lists, name='post_lists_alt'),
    path('post_details/<int:pk>/', views.post_details, name='post_details'),
    path('post_edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='post_delete'),

    # API Endpoints
    path('api/posts/', views.api_post_list, name='api_post_list'),
    path('api/posts/<int:pk>/', views.api_post_detail, name='api_post_detail'),
    path('api/posts/<int:post_id>/comments/', views.api_comment_list, name='api_comment_list'),
    path('api/comments/<int:comment_id>/', views.api_comment_detail, name='api_comment_detail'),
]