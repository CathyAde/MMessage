from django.db import models 

class member(models.Model):
    nom = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128) 
   
    




