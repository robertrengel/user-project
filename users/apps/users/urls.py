from django.contrib import admin
from django.urls import path
from . import views

app_name = "user_app"

urlpatterns = [
    path('user_register/', views.UserRegisterview.as_view(), name="user_register"),
    
]