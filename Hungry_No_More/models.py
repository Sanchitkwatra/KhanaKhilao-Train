from django.db import models
from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm


class User(AbstractUser):
    is_vendor=models.BooleanField(default=False)
    is_ngo=models.BooleanField(default=False)
    station = models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    phone_no=models.IntegerField()

    def __str__(self):
        return self.name

class NGO(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    station=models.CharField(max_length=10)
    def __str__(self):
        return self.user.name

class Vendor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    def __str__(self):
        return self.user.name
#
# class Station(models.Model):
#     station_code=models.CharField(max_length=20)

# Create your models here.
class FoodDetails(models.Model):
    train=models.IntegerField()
    station=models.CharField(max_length=200)
    veg=models.IntegerField()
    nonveg=models.IntegerField()
    claimed=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)
    ngo=models.ForeignKey(NGO,on_delete=models.CASCADE,null=True,blank=True)
    vendor=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    def __str__(self):
        return self.station
#  #def save(self,*args,**kwargs):





