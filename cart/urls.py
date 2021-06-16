from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('add<int:id>',v.add_to_cart,name='addToCart'),
    path('add_trend<int:id>',v.add_to_cart_trend,name='addToCartTrend'),
    path('add_dis<int:id>',v.add_to_cart_dis,name='addToCartDis'),
    path('-list',v.cart_list,name='List'),
    path('delete<int:id>',v.delete_cart,name='delete'),
    path('delTrend<int:id>',v.delete_cart_trend,name='deleteTrend'),
    path('deleteDis<int:id>',v.delete_cart_dis,name='deleteDis'),
]