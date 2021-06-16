from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from django.db.models.fields import files
# Create your models here.

class UserInfo(User):
    contact=models.CharField(max_length=30)
    gender=models.CharField(max_length=30)
    balance=models.IntegerField()

    class Meta:
        db_table='userinfo'
    
class UserInfoForm(UserCreationForm):
    class Meta:
        model=UserInfo
        fields=['first_name','last_name','email','contact','gender','username','password1','password2','balance']