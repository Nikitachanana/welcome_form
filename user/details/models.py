from django.db import models
from datetime import datetime

class UserDetails(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=40 )
    username = models.CharField(max_length=40, unique=True)
    password = models.CharField(max_length=40)
    photo = models.ImageField(upload_to='images/',)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    skills = models.TextField()
    joined = models.DateTimeField(default=datetime.now(), blank=True)
    empStatus = models.CharField(max_length=30)

class CardDetails(models.Model):
    id = models.ForeignKey(UserDetails,  default=1, on_delete=models.SET_DEFAULT,primary_key=True)
    cardNUmber = models.CharField(max_length=16)
    expiryDate = models.Field(max_length=13)
    cvv = models.CharField(max_length=3)



class OrderDetails(models.Model):
    id = models.ForeignKey(UserDetails,  default=1, on_delete=models.SET_DEFAULT,primary_key=True)
    ordeId = models.CharField(max_length=12, unique=True)
    trackingID = models.CharField(max_length=40)
    item = models.CharField(max_length=50)
    orderDate = models.DateTimeField()




