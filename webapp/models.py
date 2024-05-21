from django.db import models

# Create your models here.
class Customer(models.Model):
    date_creation = models.DateTimeField( auto_now_add=True)
    prenom = models.CharField(max_length=150)
    nom = models.CharField(max_length=150)
    email = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    adresse = models.CharField(max_length=500)
    ville = models.CharField(max_length=150)

    province = models.CharField(max_length=150)

    pays = models.CharField(max_length=150)


    def __str__(self):
        return f"{self.prenom}  {self.nom}"