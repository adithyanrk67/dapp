# project/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('user_details/', views.user_details, name='user_details'),  # Change the URL pattern to accept strings
]

