#autofeed
#Andrew
#27/09/2024


containerWeights = []

def get_food_weights():
    total_weight = 0
    for i in range (5):
        containerWeight = int(input(f"Please enter the weight of food in container {i+1}. If none, say '0': "))
        while containerWeight<0 or containerWeight>200:
            print("Please enter a valid weight in grams, 0-200.")
            containerWeight = int(input(f"Please enter the weight of food in container {i+1}. If none, say '0': "))
        containerWeights.append(containerWeight)
        total_weight += containerWeight
    return total_weight

def get_dog_size():
    print("""Please enter your dog size.\n1 for small.\n2 for medium.\n3 for large.\n""")
    dog_size = int(input("Either 1, 2, or 3: "))
    while dog_size<1 or dog_size>3:
        print("invalid answer, try again.")
        dog_size = int(input("Either 1, 2, or 3: "))
    if dog_size==(1) and totalWeight>=110 and totalWeight<=140:
        return("This weight is suitable")
    elif dog_size==(2) and totalWeight>=330 and totalWeight<=440:
        return("This weight is suitable.")
    elif dog_size==(3) and totalWeight>=690 and totalWeight<=900:
        return("This weight is suitable.")
    else:
        return("This weight of food is not recommended for the size of your dog.")

def find_average_weight():
    averageWeight = totalWeight/5
    averageWeight = round(averageWeight, 1)
    return averageWeight

def display_results(tw, aw, ds):
    for i in range(5):
        print(containerWeights[i])
    print(f"The total weight of food is {tw}")
    print(f"the average weight of food is {aw}")
    print(ds)



totalWeight = get_food_weights()
dogSize = get_dog_size()
averageWeight = find_average_weight()
display_results(totalWeight, averageWeight, dogSize)