from django.shortcuts import render
import matplotlib.pyplot as plt
from django.http import HttpResponse
import pandas as pd
from bs4 import BeautifulSoup
# Create your views here.
def plotdynef_view(request):
    
    data = pd.read_csv('voltocms/files/Dyneff.csv')
    
    fig, ax = plt.subplots()

    # Add a line to the plot
    ax.plot(data['Date Fin'],data['prix'])
    #add title to the plot
    ax.set_title('Dyneff')
    #add label to the x axis
    ax.set_xlabel('Date')
    ax.set_ylabel('Prix')

    # Render the plot as a PNG image and return it as an HTTP response
    response = HttpResponse(content_type='image/png')
    fig.savefig(response, format='png')
    
    return response

def visualize_xml(request):
    """
    
    """
    prix = []
    date = []
    with open("voltocms/files/Total.xml") as fp:
        soup = BeautifulSoup(fp, 'xml')

    for total in soup.find_all('row'):
        prix.append(total.find('prix').text)
        date.append(total.find('DateDebut').text)
        
    fig, ax = plt.subplots()
    ax.plot(date,prix)
    ax.set_title('Total Energy')
    ax.set_xlabel('Date')
    ax.set_ylabel('Prix')
    response = HttpResponse(content_type='image/png')
    fig.savefig(response, format='png')
    return response