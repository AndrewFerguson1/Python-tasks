# RECAP - UFO
# Original task by Mr Neil, adapted by Mr Simpson

import csv
thisDate = []
country = []
location = []
shape = []
description = []
filePath = '/workspaces/Python-tasks/sdd tasks and revision/'

numSightings = 0
numYear = 0

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

# --------------------------------------------------------------
# Task 1 functions count and display
def countSightings(country,specifiedCountry):
    numSightings = 0
    for i in range(len(country)):
        if country[i]==specifiedCountry:
            numSightings+=1
    return numSightings

def displaySightings(specifiedCountry, numSightings):
    print(f"There were {numSightings} in {specifiedCountry}.")

# --------------------------------------------------------------
 
# Task 2
def countYearSightings(thisDate):
    numYear = 0
    for i in range(len(thisDate)-1):
        thisYear = thisDate[i][6:10]
        nextYear = thisDate[i+1][6:10]
        if thisYear==nextYear:
            numYear+=1
        else:
            print(f"{thisYear}: {numYear}")
            numYear = 0


# Task 3
def findLocation(location, thisDate, shape, description):
    specifiedLocation = input("Enter a location to search for: ")
    counter = 0
    found = False
    foundLocation = -1
    while counter<len(location) and found == False:
        if location[counter]==specifiedLocation:
            found = True
        else:
            counter+=1
    if found==True:
        print((f"{thisDate[counter]}, {shape[counter]}, {description[counter]}"))
    else:
        print("Sorry, that location was not found. If you'd like to try another, run again.")



# Main program

UkCountries = ["England", "Scotland", "Wales", "Northern Ireland"]

# Task 1 - count for a country and print immediately after
for i in range(len(UkCountries)):
    numSightings = countSightings(country, UkCountries[i])
    displaySightings(UkCountries[i], numSightings)

# Task 2 - 
# CountYearSightings()
# Count the sightings each year.
# IN: thisDate [ ]
# OUT:
# 
# Note: the date is stored in the dd/mm/yyyy format,
# so a sub-string will be required to extract the year.
# 
# To implement this function you will be required to look at each date.
# If a date matches the next date in the array, increment the count by 1.
# If it doesn't match, display the date and the count, then reset it

countYearSightings(thisDate)

# Task 3 MAIN program
findLocation(location, thisDate, shape, description)