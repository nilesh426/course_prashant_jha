phy = int(input("Enter the physics marks: "))
chem = int(input("Enter the chemistry marks: "))
maths = int(input("Enter the maths marks: "))  

total = phy+chem+maths

percentage= total/3.0

gender = input("Enter your gender: ")

if percentage>=60 and gender=="male":
    print("You are eligible for placement")
else:
    print("You are eligible for data entry job")

