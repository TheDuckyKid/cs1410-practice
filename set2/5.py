"""
5. Complex Grading System
Write a program that assigns a grade based on a student's score and participation level.

Input Variables:
score (integer): The student’s score (0-100).
participation (string): The student’s participation level ("excellent", "above average", "average", or "poor").
homework_completed (boolean): Whether the student completed all homework (True or False).
Grading Rules:
If the score is 90 or above:
    If participation is excellent, grade is "A+".
    Otherwise, grade is "A".
If the score is between 80 and 89:
    If participation is above average, grade is "B+".
    Otherwise, grade is "B".
If the score is between 70 and 79:
    If the student turned in all homework, grade is "C+".
    Otherwise, grade is "C".
If the score is below 70:
    If participation is poor, grade is "F".
    Otherwise, grade is "D".
"""
score = int(input("Please input the students score: "))
participation = input("Please choose said students part")
homework_completed = input("")
pr = "placeholder"

if homework_completed.lower() == "yes" or homework_completed.lower() == "y":
    homework_completed = True
elif homework_completed.lower() == "no" or homework_completed.lower() == "n":
    homework_completed = False

if score >= 90:
    if participation == pr:
        print("Students grade is an A+")
    else:
        print("Students grade is an A")
elif score >= 80 and score <=89:
    if participation == pr:
        print("Students grade is an B+")
    else:
        print("Students grade is an B")
elif score >= 70 and score <= 79:
    if homework_completed == True:
        print("Students grade is an C+")
    else:
        print("Students grade is an C")
elif score <= 70:
    if participation == pr:
        print("Students grade is an F")
    else:
        print("Students grade is an D")