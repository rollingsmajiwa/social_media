from django.urls import path
from landing_app.views import Index, login_view, register
urlpatterns = [
    path('', Index, name='index' ),
    path('register/', register, name='register'),
    path('login/', login_view, name='login')

]