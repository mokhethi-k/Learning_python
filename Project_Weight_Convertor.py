# This program asks the user to enter their weight ib either kg or lbs and convert it if need to be
weight = int(input("Please enter your weight: "))
units = input("Is your weight in 'KG' or 'lbs' ?: ")

if units.lower() == "k":
    print(f"You are {weight} kg.")
elif units.lower() == "l":
    weight = weight * 0.45
    print(f"You are {weight} lbs.")
    