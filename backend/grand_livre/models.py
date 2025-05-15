from django.db import models
from associations.models import Associations

# Create your models here.

class GrandLivre(models.Model):
    asso = models.ForeignKey(Associations, on_delete=models.CASCADE)
    numero_compte = models.IntegerField()
    libelle = models.CharField(max_length=100)
    piece_justificative = models.CharField(max_length=100)
    debit = models.FloatField()
    credit = models.FloatField()
    
