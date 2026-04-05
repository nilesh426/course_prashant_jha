import sys
def add():
    val1=int(input("Enter the value of val1: "))
    val2=int(input("Enter the value of val2: "))
    print("Add=",val1+val2)

def sub():
    val1=int(input("Enter the value of val1: "))
    val2=int(input("Enter the value of val2: "))
    print("Sub=",val1-val2)

def mul():
    val1=int(input("Enter the value of val1: "))
    val2=int(input("Enter the value of val2: "))
    print("Mul=",val1*val2)

def div():
    val1=int(input("Enter the value of val1: "))
    val2=int(input("Enter the value of val2: "))
    if val2 !=0:
     print("Div=",val1/val2)
    else:
     print("Cannot divide by zero")

while True:
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        add()
    elif choice==2:
        sub()
    elif choice==3:
        mul()
    elif choice==4:
        div()
    elif choice==5:
        sys.exit()
    else:
        print("Invalid choice")