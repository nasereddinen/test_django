from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import  *


class UserSerializer(serializers.ModelSerializer):
    
    """
    class CompteSerializer pour serilizer le model Compte d'utilisateur
   
    """
    class Meta:
        model = UserAccount
        fields = '__all__'
        
class UserRegistration(serializers.ModelSerializer):
    """
    class UserRegistration pour enregistrer un utilisateur
    """
    class Meta:
        model = UserAccount
        fields = ('email', 'password', 'username', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserAccount.objects.create_user(**validated_data)
        return user

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        
        user = authenticate(**data)
        if user and user.is_active:
            return user
        
        raise serializers.ValidationError("Incorrect Credentials")
        
