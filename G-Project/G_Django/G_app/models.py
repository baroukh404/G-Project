from django.db import models

class user(models.Model):
    Firstname = models.CharField(max_length=255)
    Lastname = models.CharField(max_length=255)
    Phone = models.IntegerField()
    Email = models.CharField(max_length=255)
    Password = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.Firstname} {self.Lastname}"


class group(models.Model):
    invite = models.CharField(max_length=255)
    admin = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.invite} {self.admin}"