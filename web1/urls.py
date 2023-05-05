from django.contrib import admin
from django.urls import path,include
from . import views 
urlpatterns = [
    path('', views.home, name = 'home'),
    path('base/', views.base,name='base'),
    path('login/', views.login,name='login'),
    path('signup', views.signup,name='signup'),
    path('register', views.register, name='register'),
    
]    