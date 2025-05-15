from django.shortcuts import render
from rest_framework import viewsets
from .models import Associations
from .serializers import AssociationsSerializer

# Create your views here.

class AssociationsViewSet(viewsets.ModelViewSet):
    queryset = Associations.objects.all()
    serializer_class = AssociationsSerializer