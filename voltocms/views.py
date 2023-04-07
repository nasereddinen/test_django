from django.shortcuts import render
from .serializers import (
    CompanySerializer,
    CounterSerializer,
    ContratSerializer,
    CalculationSerializer
    )
from .models import *
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,RetrieveAPIView,
    RetrieveUpdateAPIView
    )
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .utils import (
    remplir_dyneff,
    xmlremp_total,
    calculate_energy_consumption)




class CreateCompanyView(GenericAPIView):
    """
    class RegisterationView pour l'enregistrement d'utilisateur
    """
    serializer_class = CompanySerializer
    permission_classes = (AllowAny,)
    
    def perform_create(self, serializer):
        serializer.save(compte = self.request.user)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(compte = request.user)
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)
        
class CompanyAccountView(ListAPIView):
    """
    class RegisterationView pour l'enregistrement d'utilisateur
    """
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)
    
    
    def get_queryset(self):
        queryset = Company.objects.all()
        compte_id = self.request.query_params.get('compte_id')
        if compte_id is not None:
            queryset = queryset.filter(compte=compte_id)
        return queryset

class GetCompanyWithSiretView(RetrieveAPIView):
    """
    class RegisterationView pour l'enregistrement d'utilisateur
    """
    serializer_class = CompanySerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'siret'
    
    def get_queryset(self):
        queryset = Company.objects.all()
        return queryset

class AddCounterView(GenericAPIView):
    """
    class RegisterationView pour l'enregistrement d'utilisateur
    """
    serializer_class = CounterSerializer
    permission_classes = (IsAuthenticated,)
    

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=400)

class GetEnergyCounterWithCompanyView(ListAPIView):
    """
    class RegisterationView pour l'enregistrement d'utilisateur
    """
    serializer_class = CounterSerializer
    permission_classes = (IsAuthenticated,)
    queryset = EnergyCounter.objects.all()
    
    def get(self,request,company_id):
        counters = self.queryset.filter(company=company_id)
        serializer = self.serializer_class(counters,many=True)
        return Response(serializer.data, status=200)
    
class GetEnergyCounterWithAccountView(ListAPIView):
    """
    class RegisterationView pour l'enregistrement d'utilisateur
    """
    serializer_class = CounterSerializer
    permission_classes = (IsAuthenticated,)
    queryset = EnergyCounter.objects.all()
    
    def get(self,request,account_id):
        
        counters = self.queryset.filter(company__compte=account_id)
        serializer = self.serializer_class(counters,many=True)
        return Response(serializer.data, status=200)



class CalculateEnergyConsumptionView(APIView):
    """
    pour calculer la consommation d'énergie
    """
    serializer_class = CalculationSerializer
    permission_classes = (IsAuthenticated,)
    
    
    def post(self,request):
        
        serializer = self.serializer_class(data=request.data,context={'choices': CalculationSerializer.TYPE_CHOICES})
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data["company"])
            company = get_object_or_404(Company, siret=serializer.validated_data["company"])
            if serializer.validated_data["type"] == "elec":
                
                dynef = Dynef.objects.create(prix=serializer.validated_data["price"],date_debut=serializer.validated_data["start_date"],date_fin=serializer.validated_data["end_date"])
                dynef.save()
                tot,created= TotalEnergy.objects.get_or_create(
                    prix=0,
                    date_debut=serializer.validated_data["start_date"],
                    date_fin=serializer.validated_data["end_date"]
                    )
                #creer un object historique
                result = serializer.to_representation(serializer.validated_data)
            
                history = EnergyHistory.objects.create(
                company=company,
                result=float(result['result']),
                dynef=dynef,
                total_energie = tot
                )
                history.save()
            elif serializer.data.get("type") == "gaz":
                tot = TotalEnergy.objects.create(prix=serializer.validated_data["price"],date_debut=serializer.validated_data["start_date"],date_fin=serializer.validated_data["end_date"])
                tot.save()
                dynef,created = Dynef.objects.get_or_create(prix=0,date_debut=serializer.validated_data["start_date"],date_fin=serializer.validated_data["end_date"])
                #creer un object historique
                result = serializer.to_representation(serializer.validated_data)
            
                history = EnergyHistory.objects.create(
                company=company,
                result=float(result['result']),
                dynef=dynef,
                total_energie = tot
                )
                history.save()
        else:
            result = serializer.errors
        
        return Response(result, status=200)
    

class AddFilesView(GenericAPIView):
    """
    class RegisterationView pour l'enregistrement d'utilisateur
    """
    

    def get(self, request):
        # pour remplir la table dyneff avec les valeurs de la fichier csv
        remplir_dyneff()
        # pour remplir la table total avec les valeurs de la fichier xml
        xmlremp_total()
        return Response("Remplissage ok", status=200)
        
        

