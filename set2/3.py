"""
3. Shopping Discount System
Write a program to calculate the final price of a shopping cart based on the following rules:
Input Variables:
    total_amount (float): Total price of items in the shopping cart.
    total_items (integer): Number of items in the shopping cart.
    is_member (boolean): Whether the customer is a member (True or False).
    is_first_time_buyer (boolean): Whether the customer is a first-time buyer (True or False).
Discount Rules:
    If the total amount is greater than $200:
        If the customer is a member, apply a 20% discount.
        Otherwise, apply a 10% discount.
    If the total amount is between $100 and $200:
        Apply a 5% discount.
        If the total items are more than 5, apply an additional $10 off.
    If the total amount is less than $100:
        If the customer is a first-time buyer, apply a flat $5 discount.
"""
total_amount = float(input("Please input the total price: "))
total_items = int(input("Please input the number of items in the cart: "))
is_member = input("Are you a member?: ")
is_first_time_buyer = input("Are you a First Time Buyer?: ")

if is_member.lower() == "yes" or is_member.lower() == "y":
    is_member = True
elif is_member.lower() == "no" or is_member.lower() == "n":
    is_member = False
if is_first_time_buyer.lower() == "yes" or is_first_time_buyer.lower() == "y":
    is_first_time_buyer = True
elif is_first_time_buyer.lower() == "no" or is_first_time_buyer.lower() == "n":
    is_first_time_buyer = False
if total_amount >=  200:
        if is_first_time_buyer == True: 
            dsc = total_amount * .20
            total_amount -= dsc
            print("Your total is now " + str(total_amount))
        else:
            dsc = total_amount * .10 
            total_amount -= dsc
            print("Your total is now " + str(total_amount))
elif total_amount >= 100 and total_amount >= 199:
    dsc = total_amount * .05
    total_amount -= dsc
    if total_items >= 5:
        total_items -= 10
        print("Your total is now " + str(total_amount))
    else:
        print("Your total is now " + str(total_amount))
elif total_amount <= 99.99:
    if is_first_time_buyer == True:
        total_amount -= 5
        print("Your total is now " + str(total_amount))
    elif is_first_time_buyer == False:
        print("Your total is now " + str(total_amount))