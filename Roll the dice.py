import random

class Roll_dice:

    def dice_1(self):
       num1 = random.randint(1,6)
       num2 = random.randint(1,6) 
       return num1,num2
   
    
first = Roll_dice()

print(first.dice_1())           