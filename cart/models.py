from django.db import models
from django.contrib.auth.models import User
from books.models import BookInfo,BookDiscount,BookTrending

# Create your models here.
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    class Meta:
        db_table='cart'

class CartDiscount(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(BookDiscount,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    class Meta:
        db_table='cart_dis'
    
class CartTrend(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    book=models.ForeignKey(BookTrending,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    class Meta:
        db_table='cart_trend'

