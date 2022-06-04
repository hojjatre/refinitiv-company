from django.urls import path
from rest_framework import views
from account import views

urlpatterns = [
    path('login/', views.login.as_view(), name='login-user'),
    path('register/', views.Register.as_view(), name='register-user'),
    path('show/', views.ShowUser.as_view(), name='show-user')
]