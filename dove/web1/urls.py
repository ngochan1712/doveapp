from django.contrib import admin
from django.urls import path,include
from . import views 
urlpatterns = [
    path('', views.home, name = 'home'),
    path('todolist', views.todolist,name='todolist'),
    path('login', views.login,name='login'),
    path('signup', views.signup,name='signup'),
    path('diemtb', views.diemtb,name='diemtb'),

]    