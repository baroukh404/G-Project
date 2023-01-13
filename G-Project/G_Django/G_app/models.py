from django.db import models

class user(models.Model):
    Firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    Phone = models.IntegerField(max_length=10)
    
    
