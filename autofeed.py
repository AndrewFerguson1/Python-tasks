#autofeed
#Andrew
#27/09/2024

totalWeight = 0
containerWeights = []
for i in range (5):
    containerWeight = int(input(f"Please enter the weight of food in container {i+1}. If none, say '0': "))
    while containerWeight<0 or containerWeight>200:
        print("Please enter a valid weight in grams, 0-200.")
        containerWeight = int(input(f"Please enter the weight of food in container {i+1}. If none, say '0': "))
