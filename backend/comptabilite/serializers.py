from rest_framework import serializers
from .models import Comptabilite, Compte



class ComptabiliteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comptabilite
        fields = '__all__'       
        

class CompteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compte
        fields = '__all__'