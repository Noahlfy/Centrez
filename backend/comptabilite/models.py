from django.db import models
from associations.models import Associations
from django.contrib.auth.models import User

# Create your models here.

class Compte(models.Model):
    numero = models.IntegerField(primary_key=True)
    categorie = models.CharField(max_length=100)   
    
    def __str__(self):
        return f"{self.numero} - {self.categorie}"
    
class Comptabilite(models.Model):
    association = models.ForeignKey(Associations, on_delete=models.CASCADE)
    date = models.DateField()
    numero_compte = models.ForeignKey(Compte, on_delete=models.PROTECT)
    libelle = models.CharField(max_length=100)
    piece_justificative = models.CharField(max_length=100)
    debit = models.FloatField()
    credit = models.FloatField()
    editeur = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.date} - {self.numero_compte} - {self.debit} / {self.credit}"