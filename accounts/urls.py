from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('reg',v.register,name='register'),
    path('login',v.log_in,name='login'),
    path('logout',v.log_out,name='logout'),
    path('edit',v.edit_user,name='edit'),
]