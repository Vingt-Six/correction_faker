from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    email = models.EmailField()
    date_embauche = models.DateField()
    salaire = models.IntegerField()
    departement = models.CharField(max_length=50)