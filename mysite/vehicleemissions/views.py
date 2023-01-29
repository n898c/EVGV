from django.shortcuts import render

import csv

from django.shortcuts import render, redirect
# Create your views here.
from .forms import CarForm
def home(request):
    
    return render(request, 'home.html', {})


def new(request):
   

    form=CarForm()
    return render(request, 'home.html', {'form':form})


def aboutus(request):
    return render(request, 'aboutus.html', {})


def resultsPage(request):
    if request.method == 'POST':
        form=CarForm(request.POST)
        modelName=request.POST.get('carModel')
        makeName=request.POST.get('make')
        makeName2=request.POST.get('make2')
        modelName2=request.POST.get('carModel2')


        carMpg=modelMPG(modelName,makeName)
        carMpg=int(float(carMpg))


        carMpg2=modelMPG(modelName2,makeName2)
        
        #carMpg2=int(float(carMpg2))

        carCO=COperYear(modelName,makeName)
        carCO=int(float(carCO))


        carCO2=COperYear(modelName2,makeName2)

        print("CAR CO: ",carCO)
        #carCO2=int(float(carCO2))


        carMpg=((12000/int(carMpg))*3.5)
        #carMpg2=((12000/int(carMpg2))*3.5)

        carCO=(12000*float(carCO))/1000000
        #carCO2=(12000*float(carCO2))/1000000






        
        #carMpg2=(12000/int(carMpg2))*3.5
       # carCO=(12000*int(carCO))
        return render(request, 'results.html', {'carMpg':carMpg,'carMpg2':carMpg2,'carCO':carCO,'carCO2':carCO2,'makeName':makeName,'makeName2':makeName2,'modelName':modelName,'modelName2':modelName2})

   

import csv
def modelMPG(modelName,makeName):
    
    with open('C:/Users/omuza/OneDrive/Desktop/hackaton/mysite/vehicleemissions/carlist.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            
            if ((row[1]).upper())==makeName.upper() and str(row[4]).upper()==modelName.upper():
                
                return (row[45])
        else:
            print("not found")


def COperYear(modelName,makeName):

    with open('C:/Users/omuza/OneDrive/Desktop/hackaton/mysite/vehicleemissions/carlist.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            
            if str(row[1]).upper()==makeName.upper() and str(row[4]).upper()==modelName.upper():
                if (row[40]==""):
                    return 0
                return row[40]
        else:
            print("not found")







