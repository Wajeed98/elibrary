from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('byId<int:id>',v.sort_by_category,name='sortByID'),
    path('search',v.search_books,name='search'),
]