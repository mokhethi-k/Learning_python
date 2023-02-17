"""
for every character in the original string, 
return triple the character.
e.g python - pppyyyttthhhooonnn    
"""

def triple(str):
    word = ""
    for i in str:
        word += i*3
    return word

word = input("Enter a word: ")
print(triple(word))