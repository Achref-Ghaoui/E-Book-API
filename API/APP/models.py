from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
    titre=models.CharField(max_length=20)
    description=models.CharField(max_length=20,blank=True,null=True)
    auteur =models.CharField(max_length=20,null=True,blank=False)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
