from django.db import models
from django.
# Create your models here.
class persons(models.Model):
    user=
    name=models.CharField(max_length=100)
    phone_no=models.IntegerField(max_length=15)
    