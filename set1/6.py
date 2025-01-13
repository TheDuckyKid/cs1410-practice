#check persons ability to vote
quacl = int(input("Please type a number "))
if quacl >= 18:
    print("You can vote")
elif quacl <= 17:
    print("You can't vote wait a few years")