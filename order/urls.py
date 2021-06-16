from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('list',v.get_order_list,name='List'),
    path('delete<int:id>',v.delete_order,name='deleteOrd'),
]