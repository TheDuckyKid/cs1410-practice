"""
4. Tax Calculator
Write a program that calculates the tax owed based on income and other factors.

Input Variables:
income (float): Total yearly income.
is_married (boolean): Whether the person is married (True or False).
has_dependents (boolean): Whether the person has dependents (True or False).
owns_business (boolean): Whether the person owns a business (True or False).
Tax Rules:
If the income is less than $30,000:
    If they are single, tax is 10%.
    If they are married, tax is 8%.
If the income is between $30,000 and $100,000:
    If they have dependents:
        15% tax for single.
        12% tax for married.
    If they have no dependents, tax is 18%.
If the income is above $100,000:
    If they own a business, tax is 25%.
    Otherwise, tax is 28%.
"""
income = float(input("What is your yearly income? "))
is_married = input("Are you married? ")
has_dependents = input("Do you have Dependents? ")
owns_business = input("Do you own a business? ")

if has_dependents.lower() == "yes" or has_dependents.lower() == "y":
    has_dependents = True
elif has_dependents.lower() == "no" or has_dependents.lower() == "n":
    has_dependents = False

if owns_business.lower() == "yes" or owns_business.lower() == "y":
    owns_business = True
elif owns_business.lower() == "no" or owns_business.lower() == "n":
    owns_business = False

if income <= 29999:
    if is_married == False:
        print("Your tax is 10%")
    elif is_married == True:
        print("Your tax is 8%")
elif income <= 100000:
    if has_dependents == True:
        if is_married == False:
            print("Your tax is 15%")
        if is_married == True:
            print("Your tax is 12%")
    elif has_dependents == False:
        print("Your tax is 18%")
elif income >= 100001:
    if owns_business == True:
        print("Your tax is 25%")
    else:
        print("Your tax is 28%")