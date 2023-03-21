#import modules that we will use

import csv
import copy

#define dictionary, will serve composite type for reading tabular data:

myVehicle- {
    "vin" : "<empty>",
    "make" : "<empty>",
    "model" : "<empty>",
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}

#For loop : itirate over initial key and value of dictionary

for key, value in myVehicle.items():
    print("{} : {}".format(key, value))
    
#deine empty list: to hold car inventory that will be read.

myInventoryLists = []


# imp commands used 

# with open : this command keeps file open during read
#with : this command closes .csv file when code ends
# csv.reader() : command from csv library, that was imported with command 
              # import.csv
              
              
with open('car_fleet.csv') as csvFile:
    csvReader = csv.reader(csbFile, delimiter-',')
    lineCount = 0
    for row in csvReader:
        if lineCount == 0:
            print(f'Column names are : {", ".join(row)}')
            lineCount += 1
            else:
                print(f'vin : {row[0]}, make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')
                currentVehicle = copy.deepcopy(myVehicle)
                currentVehicle["vin"] = row[0]
                currentVehicle["make"] = row[1]
                currentVehicle['model'] = row[2]
                currentVehicle["year"] = row[3]
                currentVehicle["range"] = row[4]
                currentVehicle["topSpeed"] = row[5]
                currentVehicle["zeroSixty"] = row[6]
                currentVehicle["mileage"] = row[7]
                myInventoryLists.append(currentVehicle)
                lineCount += 1
    print(f'Processed {lineCount} lines.')
    
    
    #Printing the car inventory
    
    for myCarProperties in myInventoryLists:
        for key, value in myCarProperties.items():
            print ("{} : {}".format(key, value))
            print("------")
    
    