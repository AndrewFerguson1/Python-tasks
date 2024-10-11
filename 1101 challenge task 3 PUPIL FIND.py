# TASK
# Create a program which reads in a list of pupil names from a text file and then asks the user to enter a name.
# If their name matches one in the list, display an appropriate message.
# If their name does not match one in the list, add this to the text file.
# Andrew Ferguson
# 10 October 2024
names = []
with open("students.txt","r") as readFile:
    line = readFile.readline().rstrip('\n')
    while line:
        names.append(line)
        line = readFile.readline().rstrip('\n')
userName = input("Hello, what is your name? Enter here: ")

