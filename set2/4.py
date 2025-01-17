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