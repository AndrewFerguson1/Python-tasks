#autofeed
#Andrew
#27/09/2024

totalWeight = 0
containerWeights = []
dog_size = 0

def get_food_weights():
    for i in range (5):
        containerWeight = int(input(f"Please enter the weight of food in container {i+1}. If none, say '0': "))
        while containerWeight<0 or containerWeight>200:
            print("Please enter a valid weight in grams, 0-200.")
            containerWeight = int(input(f"Please enter the weight of food in container {i+1}. If none, say '0': "))

def enter_dog_size():
    print("""Please enter your dog size.\n1 for small.\n2 for medium.\n3 for large.\n""")
    dog_size = int(input("Either 1, 2, or 3: "))
    while dog_size<0 or dog_size>3:
        print("invalid answer, try again.")
        dog_size = input("Either 1, 2, or 3: ")
enter_dog_size()
print(dog_size)