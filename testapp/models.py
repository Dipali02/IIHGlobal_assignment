from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    dob=models.DateField(max_length=20,null=True)
    profile_pic=models.ImageField(null=True,blank=True)
    fees=models.IntegerField(null=True)
