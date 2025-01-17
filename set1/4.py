#rumber range 1-10 or 11-20
print("Please type in a number to be ranged? ")
quacl = int(input())
if quacl <= 10 or quacl <= 1:
    print("this number is in the 0-10 range")
elif quacl <= 20 or quacl <= 11:
    print("this number is in the 11-20 range")
else:
    print("This number isnt in any of the predetermined ranges")