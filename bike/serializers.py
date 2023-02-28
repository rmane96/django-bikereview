from rest_framework import serializers
from bike.models import Bike


class BikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Bike
        fields = '__all__'
    
    