# triangle app
chicken = int(input("Give me the first side of the triangle: "))
chicken2 = int(input("Give me the second side of the triangle: "))
chicken3 = int(input("Give me the third side of the triangle: "))
if chicken + chicken2 > chicken3:
    print("You made a triangle")
elif chicken + chicken3 > chicken2:
    print("You made a triangle")
elif chicken2 + chicken3 > chicken:
    print("You made a triangle")
else:
    print("Thats not a triangle")