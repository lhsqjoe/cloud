# -*- coding: utf-8 -*-
from django.urls import path
from . import views

app_name = "webconsole" #URL 命名空间

urlpatterns = [
    path('', views.show_login, name='show_login'),
    path('login/', views.login, name='login'),
    path('logout/', views.log_out, name='logout')

]