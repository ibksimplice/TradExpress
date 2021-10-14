from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    buisness = models.CharField(max_length=10,blank = True,null=True,)
    individual = models.CharField(max_length=10,blank = True, null=True)
    fullname = models.CharField(max_length=50)
    phonenumber = models.CharField(max_length=50)
    referral_code = models.CharField(max_length=10,blank = True, null = True,)