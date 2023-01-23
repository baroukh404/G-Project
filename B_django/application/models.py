from django.db import models

class users(models.Model):
	Firstname = models.CharField(max_length=255)
	Lastname = models.CharField(max_length=255)
	Phone = models.IntegerField(max_length=255)
	Email = models.CharField(max_length=255)
	Filiere = models.CharField(max_length=255)
	Parcours = models.CharField(max_length=255)
	
	def __str__(self):
		return f"{self.Firstname} , {self.Lastname}"
