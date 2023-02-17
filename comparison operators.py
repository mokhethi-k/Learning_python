
name = input("Please enter your name: ")

if len(name) < 3:
    print("A name cannot be less than 3 characters")
elif len(name) > 50:
    print("A name cannot be greater than 50 characters")
else:
    print("Name is good")
    