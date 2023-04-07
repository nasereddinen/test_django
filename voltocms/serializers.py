from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from authentication.models import UserAccount
from .models import *


class CompanySerializer(serializers.ModelSerializer):
    

    class Meta:
        model = Company
        fields = '__all__'

    def validate(self, data):
        """
        pour verifier si la company existe deja
        
        """
        if Company.objects.filter(siret=data['siret']).exists():
            raise serializers.ValidationError("Company already exists")
        return data
    
    
class CounterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EnergyCounter
        fields = '__all__'


class ContratSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = EnergyHistory
        fields = ('id', 'total_energie','dynef', 'company', 'date')
        

class CalculationSerializer(serializers.Serializer):
    TYPE_CHOICES = [
        ('elec', 'elec'),
        ('gaz', 'gaz'),
    ]

    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())
    counter_id = serializers.PrimaryKeyRelatedField(queryset=EnergyCounter.objects.all())
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    consumption = serializers.DecimalField(max_digits=10, decimal_places=2)
    type = serializers.ChoiceField(choices=TYPE_CHOICES)

    def validate(self, data):
        """
        verifier si la date de fin est superieur a la date de debut
        """
        if data['end_date'] <= data['start_date']:
            raise serializers.ValidationError("End date must be after start date.")
        return data

    def to_representation(self, instance):
        """
            calculer la consommation d'energie      
        """
        result = instance['price'] * instance['consumption']
        return {'result': result}