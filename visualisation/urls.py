from django.test import TestCase
from django.urls import path
import visualisation.views as views
# Create your tests here.
app_name = "visualisation"
urlpatterns = [
    path('visualisation_csv/', views.plotdynef_view, name="visualisation"),
    path('visualisation_xml/', views.visualize_xml, name="visualisation_xml"),
    
]