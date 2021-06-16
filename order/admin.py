from django.contrib import admin
from .models import Order
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display=['id','orderDate','totalBill','status','user']
    list_filter=['status','user']
    search_fields=('status',)

admin.site.register(Order,OrderAdmin)