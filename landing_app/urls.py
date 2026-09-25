from django.urls import path
from landing_app.views import Index
urlpatterns = [
    path('', Index.as_view(), name='index' ),
    
]