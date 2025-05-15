from django.shortcuts import render
from rest_framework import viewsets
from .models import GrandLivre
from .serializers import GrandLivreSerializer
# Create your views here.

class GrandLivreViewSet(viewsets.ModelViewSet) :
    queryset = GrandLivre.objects.all()
    serializer_class = GrandLivreSerializer
    

