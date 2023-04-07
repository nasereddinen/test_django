from django.db import models
from authentication.models import UserAccount

#la table company
class Company(models.Model):
    siret = models.CharField(max_length=50)
    raison_sociale = models.CharField(max_length=50)
    compte = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.siret
    
#la table compteur
class EnergyCounter(models.Model):
    
    ENERGIE_CHOICES = [
        ('elec', 'elec'),
        ('gaz', 'gaz'),
        
    ]
    numero = models.CharField(max_length=50,default="0")
    consumation = models.FloatField(blank=False, null=False, default=0)
    energie_type = models.CharField(max_length=50, choices=ENERGIE_CHOICES, default='elec')
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.numero
    
#la table total energy   
class TotalEnergy(models.Model):
    date_debut = models.DateField()
    prix = models.FloatField()
    date_fin = models.DateField()
    
    def __str__(self):
        return f"TotalEnergit {self.date_debut}-{self.date_fin}"
    
    
#la table dynef  
class Dynef(models.Model):
    prix = models.FloatField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    
    def __str__(self):
        return f"dynef {self.date_debut}-{self.date_fin}"
    
   
#le model qui va contenir les resultats de la consommation la table historique
class EnergyHistory(models.Model):
    date = models.DateField(auto_now=True)
    total_energie = models.ForeignKey(TotalEnergy, on_delete=models.CASCADE)
    result = models.FloatField(null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    dynef = models.ForeignKey(Dynef, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"EnergyHistory {self.date}"
