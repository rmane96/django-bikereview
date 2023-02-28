from django.shortcuts import render
from rest_framework import generics
from bike.models import Bike
from bike.serializers import BikeSerializer


class BikeListView(generics.ListCreateAPIView):
    serializer_class = BikeSerializer     
    queryset = Bike.objects.all()   


