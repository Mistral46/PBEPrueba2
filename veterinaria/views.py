from django.shortcuts import render
from rest_framework import viewsets
from .serializer import AnimalSerializer
from .models import Animal

# Create your views here.


class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer