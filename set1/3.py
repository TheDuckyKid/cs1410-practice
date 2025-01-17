#tell me if the number is + - or 0
print("Please type in a number.")
quacl = int(input())
numP = ""
if quacl >= 1:
    numP = "Positive or +"
elif quacl == 0:
    numP = "Zero or 0"
if quacl <= -1:
    numP = "Negative or -"
print("Your number is " +numP)