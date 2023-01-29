import csv

def modelMPG(makeName,modelName):
    
    with open('C:/Users/omuza/OneDrive/Desktop/hackaton/mysite/vehicleemissions/carlist.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            #print(row[1])
            if str(row[1]).upper()==makeName.upper() and str(row[4]).upper()==modelName.upper():
                print(row[1])
                print(row[4])
                print(row[45])
                return row[45]
                break
        else:
            print("not found")

modelMPG('Toyota','Camry')