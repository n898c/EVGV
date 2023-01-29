from django.shortcuts import render

import csv

from django.shortcuts import render, redirect
# Create your views here.
from .forms import CarForm
def home(request):
    
    return render(request, 'home.html', {})


def new(request):
    if request.method == 'POST':
        form=CarForm(request.POST)
        modelName=request.POST.get('carModel')
        makeName=request.POST.get('make')
        makeName2=request.POST.get('make2')
        modelName2=request.POST.get('carModel2')
        carMpg=modelMPG(modelName,makeName)
        carMpg2=modelMPG(modelName2,makeName2)
        carCO=COperYear(modelName,makeName)
        carCO2=COperYear(modelName2,makeName2)
        
        

       

    else:
        form=CarForm()
    return render(request, 'home.html', {'form':form})




import csv
def modelMPG(modelName,makeName):
    
    with open('C:/Users/omuza/OneDrive/Desktop/hackaton/mysite/vehicleemissions/carlist.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            
            if str(row[1]).upper()==makeName.upper() and str(row[4]).upper()==modelName.upper():
                
                return row[45]
        else:
            print("not found")


def COperYear(modelName,makeName):

    with open('C:/Users/omuza/OneDrive/Desktop/hackaton/mysite/vehicleemissions/carlist.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            
            if str(row[1]).upper()==makeName.upper() and str(row[4]).upper()==modelName.upper():
                
                return row[40]
        else:
            print("not found")







