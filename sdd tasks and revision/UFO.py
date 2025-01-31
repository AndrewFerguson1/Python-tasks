# RECAP - UFO
# Original task by Mr Neil, adapted by Mr Simpson

import csv

thisDate = []
country = []
location = []
shape = []
description = []
filePath = 'Software Design and Development/RECAP - UFO/'

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

# Task 1 Functions
def CountSightings(country_list, specified_country):
    count = 0
    for c in country_list:
        if c == specified_country:
            count += 1
    return count

def DisplaySightings(specified_country, num_sightings):
    print(f"There were {num_sightings} sightings in {specified_country}")

# Task 2 Function
def CountYearSightings(date_list):
    if not date_list:
        print("No dates available.")
        return
    
    current_year = None
    count = 0
    
    for date_str in date_list:
        year = date_str.split('/')[2]
        if current_year is None:
            current_year = year
            count = 1
        elif year == current_year:
            count += 1
        else:
            print(f"{current_year}: {count}")
            current_year = year
            count = 1
    # Print the last accumulated year
    if current_year is not None:
        print(f"{current_year}: {count}")

# Task 3 Function
def FindSightingsByLocation(location_list, date_list, shape_list, description_list):
    search_location = input("Enter a location to search for: ").strip()
    found = False
    for i in range(len(location_list)):
        if location_list[i] == search_location:
            print(f"{date_list[i]}, {shape_list[i]}, {description_list[i]}")
            found = True
    if not found:
        print(f"No sightings found in {search_location}")

# Main program
thisDate, country, location, shape, description = importFile()

# Execute Task 1
print("Task 1: Number of Sightings per Country")
uk_countries = ['England', 'Scotland', 'Wales', 'Northern Ireland']
for country_name in uk_countries:
    count = CountSightings(country, country_name)
    DisplaySightings(country_name, count)

# Execute Task 2
print("\nTask 2: Number of Sightings per Year")
CountYearSightings(thisDate)

# Execute Task 3
print("\nTask 3: Search by Location")
FindSightingsByLocation(location, thisDate, shape, description)