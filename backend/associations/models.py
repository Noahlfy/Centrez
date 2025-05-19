from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from django.contrib.auth.models import User
from django.db import models

class Associations(models.Model):
    association = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    president = models.ForeignKey(User, on_delete=models.CASCADE, related_name='president_associations')
    treasurer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='treasurer_associations')

    def __str__(self):
        return f"{self.name}"