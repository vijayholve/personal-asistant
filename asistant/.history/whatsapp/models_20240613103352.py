from django.db import models
from django.contrib.auth.models import User
class persons(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=15)
    def __str__(self) -> str:
        return f"{self.name} ------------------------------{self.phone_no}"
    
