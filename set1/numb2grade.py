#make a grade calculator?
print("Please type in a grade.")
quacl = int(input())
grade = ""
if quacl <= 59:
    grade = "F"
elif quacl <= 69:
    grade = "D"
elif quacl <= 79:
    grade = "C"
elif quacl <= 89:
    grade = "B"
elif quacl <= 100:
    grade = "A"
print("Your grade is " +grade)