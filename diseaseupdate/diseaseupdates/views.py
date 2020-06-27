from django.shortcuts import render
from .models import Diseaseupdates
from rest_framework import generics
from .serializers import DiseaseupdatesSerializer


# Create your views here.
class DiseaseupdatesListCreate(generics.ListCreateAPIView):
     queryset = Diseaseupdates.objects.all()
     serializer_class = DiseaseupdatesSerializer
