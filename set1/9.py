"""9. Discount Calculator
Write a program that calculates a discount:

10% off if the total is greater than $100
Otherwise, no discount."""
totalp = int(input("Please input your total: "))
if totalp >= 100:
    dtotal = totalp - (totalp *.10) 
    print("Discount applied your new price is: $" + str(dtotal))
else:
    print("No Discount total is: $" + str(totalp))
