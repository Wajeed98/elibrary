from django.db import models
from django.db.models.base import Model

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=50)

    class Meta:
        db_table='category'

    def __str__(s):
        return s.name

class BookInfo(models.Model):
    name=models.CharField(max_length=40)
    author=models.CharField(max_length=40)
    publisher=models.CharField(max_length=50)
    price=models.IntegerField()
    image=models.ImageField(upload_to='images',default='')
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='bookinfo'

    def __str__(s):
        return s.name

class BookDiscount(models.Model):
    name=models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    dis_price=models.IntegerField()

    class Meta:
        db_table='bookdiscount'


class BookFavourite(models.Model):
    name=models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='bookfavourite'

class BookTrending(models.Model):
    name=models.ForeignKey(BookInfo,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        db_table='booktrending'
