from rest_framework import serializers
from .models import GrandLivre


class GrandLivreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = GrandLivre
        fields = '__all__'