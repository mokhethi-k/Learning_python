names = ["henry", "alex", "tim", "alison", "ariel"]

uniques = []

for name in names:
    if name[0] == "a":
        uniques.append(name.capitalize() + " Smith")
print(uniques)