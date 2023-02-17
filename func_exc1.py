
'''
given a string  = str
you are given a positive int  = n
return n coppies of str
'''

def multiple(str, n):
    return str * n

str = input("Enter a string: ")
num = int(input("Enter a number: "))
print(multiple(str, num))