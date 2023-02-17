# This is program executes depending on whether the condition is true or false

price = 1000000
good_credit = bool(input("Does the buyer has a good credit? "))

if good_credit:
    down_price = price * 0.1
    print(f'The down price is: R{down_price}')
else:
    down_price = price * 0.2
    print(f'The down price is: R{down_price}')
