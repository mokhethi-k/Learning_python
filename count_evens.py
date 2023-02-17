'''
Count how many evens are in the list
'''

list = [2,3,5,2,5,7,-8,9,-20]
count = 0

for i in list:
    if i % 2 == 0:
        count += 1

print(f"There are {count} evens in the list")