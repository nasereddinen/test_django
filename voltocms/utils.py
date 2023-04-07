import pandas as pd
from .models import Dynef, TotalEnergy
import xml.dom.minidom as minidom
import xmltodict
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from datetime import datetime

def remplir_dyneff():
    """
    j'ai utilisé pandas mon librerie péférer pour la manipulation (csv ou xls) pour lire le fichier csv et le convertir en dataframe
    """
    dyneff_df = pd.read_csv('voltocms/files/Dyneff.csv', index_col=0)
    print(dyneff_df.columns)
    print(dyneff_df.dtypes)
    dyneff_df['prix']  = dyneff_df['prix'].str.replace(',', '.')
    dyneff_df['prix'] = dyneff_df['prix'].astype(float)
    dyneff_df['Date Debut'] = dyneff_df['Date Debut'].astype('datetime64[ns]')
    dyneff_df['Date Fin'] = dyneff_df['Date Debut'].astype('datetime64[ns]')
    dyneff_df['Date Debut'] = dyneff_df['Date Debut'].dt.strftime('%Y-%m-%d')
    dyneff_df['Date Fin'] = dyneff_df['Date Fin'].dt.strftime('%Y-%m-%d')
    
    for index,dynef in dyneff_df.iterrows():
        dynef = Dynef.objects.create(prix=dynef["prix"], date_debut=dynef["Date Debut"], date_fin=dynef["Date Fin"])
        dynef.save()
        

def xmlremp_total():
    """
    remplir la table total energy
    j'ai utilise la librairie BeautifulSoup pour parser le fichier xml
    et j'ai utilise plesieur autre librerie mais seul celle ci a marche
    
    """
    with open("voltocms/files/Total.xml") as fp:
        soup = BeautifulSoup(fp, 'xml')

    for total in soup.find_all('row'):
        print(f"prix: {total.find('DateDebut').text}")
        prix = to_float(total.find('prix').text)
        date_deb = to_date(total.find('DateDebut').text)
        date_f = to_date(total.find('DateFin').text)      
        instance = TotalEnergy.objects.create(prix=prix, date_debut=date_deb, date_fin=date_f)
        instance.save()


def to_float(string):
    string = string.replace(',', '.')
    return float(string)
#change the speparator the string to get the date in the right format
def to_date(str):
    """
    j'ai mis le / au lieu du - pour separer les jours, mois et annees
    et je appelle la fonction format_date pour changer le format de la date
    """
    strdt = str.replace('/', '-')
    return format_date(strdt)
#formatting the date to the right format
def format_date(date_str):
    date_obj = datetime.strptime(date_str,'%d-%m-%Y')
    date_formatted = date_obj.strftime('%Y-%m-%d')
    return date_formatted


def calculate_energy_consumption(date_debut,counter,consumption,siret,elec_price,gaz_price):
    """
    
    il faut que la date de debut soit inferieur a la date de fin
    et calculer la consommation d'energie
    il retourne un dictionnaire avec les valeurs suivantes(
    energy_consumption_elec,
    energy_consumption_gaz,
    energy_consumption,
    siret,
    counter
    )
    """
    energy_consumption = 0
    if date_debut == date_fin or date_debut > date_fin:
        return "la date de debut doit etre inferieur a la date de fin"
    else:
        energy_consumption_elec = consumption*elec_price
        energy_consumption_gaz = consumption*gaz_price
        result = {
            'energy_consumption_elec':energy_consumption_elec,
            'energy_consumption_gaz':energy_consumption_gaz,
            'energy_consumption':energy_consumption_elec+energy_consumption_gaz,
            'siret':siret,
            'counter':counter,
        }
        return result