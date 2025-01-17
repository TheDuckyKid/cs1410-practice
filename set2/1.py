"""
1. Movie Ticket Pricing System
Write a program to calculate the price of a movie ticket based on the following conditions:
Input Variables:
    age (integer): Age of the person.
    is_weekend (boolean): Whether it’s a weekend (True or False).
    is_student (boolean): Whether the person is a student (True or False).
Pricing Rules:
    If the person is under 12 years old, the price is $8.
    If the person is 12-17 years old:
        If it’s a weekend, the price is $12.
        If it’s a weekday, the price is $10.
    If the person is 18-64 years old:
        If it’s a weekday and the person is a student, the price is $12.
        Otherwise, the price is $15.
    If the person is 65 or older, the price is $10.
"""
age = int(input("What is your age?: "))
is_weekend = input("Is it the weekend?: ")
is_student = input("Are you a student?: ")

if is_weekend.lower() == "yes" or is_weekend.lower() == "y":
    is_weekend = True
elif is_weekend.lower() == "no" or is_weekend.lower() == "n":
    is_weekend = False

if is_student.lower() == "yes" or is_student.lower() == "y":
    is_student = True
elif is_student.lower() == "no" or is_student.lower() == "n":
    is_student = True

if age <= 12:
    print("Ticket price is $8")
elif age <= 17:
    if is_weekend == True:
        print("Ticket price is $12")
    elif is_weekend == False:
        print("Ticket price is $10")
elif age <= 64:
    if is_weekend == True and is_student == True:
        print("Ticket price is $12")
    else:
        print("Ticket price is $15")
elif age >= 65:
    print("Ticket price is $10")