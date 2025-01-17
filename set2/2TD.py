"""
2. Advanced Number Checker
Write a program that evaluates the relationship between three numbers based on multiple conditions.
Input Variables:
    num1 (integer): First number.
    num2 (integer): Second number.
    num3 (integer): Third number.
Conditions:
    Check if all three numbers are equal.
    Check if any two numbers are equal.
    Check if the numbers are in ascending order.
    Check if the numbers are in descending order.
    If none of the above conditions are true, print "No specific pattern found."
"""
num1 = int(input("Please put in a number"))
num2 = int(input("Please put in a second number"))
num3 = int(input("Please put in a third number"))

if num1 == num2 and num2 == num3:
    print("All 3 numbers are equal")
elif num1 == num2 or num3 == num2:
    print("2 Numbers are equal")
