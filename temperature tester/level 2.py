# Create a program that allows a user to:
# Enter 14 daily temperatures between -20 and +50 C and store these in a record TEMP(day, dayTemp).
# Display all temperatures and, for day 8-14, the difference between the previous week.
# Calculate and display the average temperature.
# Your program should use input validation, a 1-D array of records and fixed loops.

from dataclasses import dataclass

@dataclass
class TEMP():
    day : int = 0
    dayTemp : int = 0


temps = []

for i in range (14):
    temp = int(input(f"Please enter the temperature in celcius of day number {i+1}: "))
    while temp<-20 or temp>50:
        temp = int(input(f"Sorry! That temperature is not within the range, please enter a temperature between -20 and 50 degrees celcius for day number {i+1}: "))
    temps.append(temp)

for i in range(5):
    print (f"On day {i+1}, the temperature was {temps[i]}.")

print(f"The average temperature was {sum(temps)/len(temps)}.")