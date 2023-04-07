from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Company)
admin.site.register(Dynef)
admin.site.register(TotalEnergy)
admin.site.register(EnergyHistory)
admin.site.register(EnergyCounter)