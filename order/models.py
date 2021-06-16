from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Order(models.Model):
    totalBill=models.IntegerField()
    status=models.CharField(max_length=30,default="In-Process")
    orderDate=models.DateField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
