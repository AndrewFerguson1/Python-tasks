# RECAP - UFO
# Original task by Mr Neil, adapted by Mr Simpson

import csv
thisDate = []
country = []
location = []
shape = []
description = []
filePath = '/workspaces/Python-tasks/sdd tasks and revision/'

UkCountries = ["England", "Scotland", "Wales", "Northern Ireland"]
numSightings = 0

# -------------------------------------------------- DO NOT ALTER -----
def importFile():
    with open(filePath+'ufo_sighting.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            thisDate.append(row[0])
            country.append(row[1])
            location.append(row[2])
            shape.append(row[5])
            description.append(row[6])
    return thisDate, country, location, shape, description
# -------------------------------------------------- DO NOT ALTER -----

thisDate, country, location, shape, description = importFile()

def countSightings(country,specifiedCountry):
    numSightings = 0
    for i in range(len(country)):
        if country[i]==specifiedCountry:
            numSightings+=1
    return numSightings

def displaySightings(specifiedCountry, numSightings):
    print(f"There were {numSightings} in {specifiedCountry}.")





# Main program

# execute read csv, set variables
thisDate, country, location, shape, description = importFile()

# count for a country and print immediately after
for i in range(len(UkCountries)):
    num = countSightings(country, UkCountries[i])
    displaySightings(UkCountries[i], num)

