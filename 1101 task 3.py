items = []
names = []
marks = []
with open("pupils.txt") as readfile:
    line = readfile.readline().rstrip('\n')
    while line:
        items = line.split(",")
        names.append(items[0])
        marks.append(items[1])
        line = readfile.readline().rstrip('\n')


for counter in range(len(names)):
    print(f"{names[counter]} scored {marks[counter]} points.")


# Run the program. Now edit the code so that it displays each student name with their mark e.g. Monica - 85