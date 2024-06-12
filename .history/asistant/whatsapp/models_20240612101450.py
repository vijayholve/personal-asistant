from django.db import models

# Create your models here.
class persons(models.Model):
    name=models.CharField(max_length=100)
    phone=