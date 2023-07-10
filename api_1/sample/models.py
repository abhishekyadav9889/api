from django.db import models

# Create your models here.
class  Student(models.Model):
    fast_name=models.CharField(max_length=100)
    last_Name=models.CharField(max_length=100)
    roll_No= models.IntegerField()
    ctye=models.CharField(max_length=100)