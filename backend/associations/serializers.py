from rest_framework import serializers
from .models import Associations

class AssociationsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Associations
        fields = '__all__'