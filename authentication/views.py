from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import GenericAPIView,RetrieveUpdateAPIView
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
class RegisterationView(GenericAPIView):
    
    """
    class RegisterationView pour l'enregistrement d'utilisateur
    """
    serializer_class = UserRegistration
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = RefreshToken.for_user(user)
        data = serializer.data
        data['token'] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(serializer.data, status=200)

class LoginView(GenericAPIView):
    """
    class LoginView pour la connexion d'utilisateur en utilisant le jwt token
    """
    serializer_class = UserLoginSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        user = UserAccount.objects.get(email=data['email'])
        token = RefreshToken.for_user(user)
        data["tokens"] = {"refresh": str(token), "access": str(token.access_token)}
        return Response(data, status=200)

class UserDetailView(RetrieveUpdateAPIView):
    """
    j'ai crée cette class pour afficher les informations de l'utilisateur connecté
    pour la verification de l'utilisateur connecté avec jwt le token
    
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user