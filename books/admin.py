from django.contrib import admin
from .models import BookFavourite, BookInfo,BookDiscount,BookTrending,Category
# Register your models here.

class BookInfoAdmin(admin.ModelAdmin):
    list_display=['id','name','author','publisher','price','category']
    list_filter=['author','category','price','publisher']
    search_fields=('author','publisher','name')

class BookDiscountAdmin(admin.ModelAdmin):
    list_display=['id','name','dis_price','category']
    list_filter=['dis_price','category','name']
    search_fields=('category','name')

class BookTrendAdmin(admin.ModelAdmin):
    list_display=['id','name','category']
    list_filter=['name','category']
    search_fields=('category','name')

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','name','description']
    list_filter=['name']
    search_fields=('name',)

admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(BookDiscount,BookDiscountAdmin)
admin.site.register(BookTrending,BookTrendAdmin)
admin.site.register(Category,CategoryAdmin)

