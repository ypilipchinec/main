from django.db import models
from django.db.models.base import Model

class camers(models.Model):
    
    type=models.CharField(max_length=10)
    name = models.CharField(max_length=255)
    address = models.GenericIPAddressField(null=True,blank=True)
    link = models.CharField(max_length=255,blank=True,null=True)
    guid = models.CharField(max_length=255)
  
  
class files(models.Model):

    name = models.CharField(max_length=20, null=True, blank=True)
    dir_path = models.CharField(max_length=255, null=True, blank=True)
    file = models.CharField(max_length=255, default=0, null=True)
    status = models.BooleanField(null=True)   
    create_at = models.DateTimeField(null=True, blank=True)

    
