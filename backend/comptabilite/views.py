from django.shortcuts import render
from rest_framework import viewsets
from .models import Comptabilite, Compte
from .serializers import ComptabiliteSerializer, CompteSerializer
# Create your views here.

class ComptabiliteViewSet(viewsets.ModelViewSet) :
    queryset = Comptabilite.objects.all()
    serializer_class = ComptabiliteSerializer
    

class CompteViewSet(viewsets.ModelViewSet):
    queryset = Compte.objects.all()
    serializer_class = CompteSerializer