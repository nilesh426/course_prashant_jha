# Data structures are diiferent ways of organizing data in a computer memory that can be used effectively.

#stack implementation with size limit
import sys
class Stack:
    def __init__(self,stacksize): #parameterized constructor
        self.stacklist=[]
        self.stacksize=stacksize

    def isfull(self):
        if len(self.stacklist)==self.stacksize:
            return "Stack is full"
        else:
            return "Stack is not full"

    def push(self,value):
        if self.isfull():
            print("stack is full")
        else:
            self.stacklist.append(value)

    def isEmpty(self):
        if self.stacklist==[]:
            print("Stack is empty")
        else:
            print("Stack is not empty")
        
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.stacklist.pop()
        
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            return self.stacklist[-1]
        
    def deletestack(self):
        self.stacklist=[]
        print("Stack is deleted")

    def displaystack(self):
         print("======================")
         print(self.stacklist)
         print("======================")

size=int(input("Enter the size of stack: "))
stackobj = Stack(size)

while True:
    print("1.Push Element in Stack")
    print("2.Display stack elements")
    print("3.Is the stack empty")
    print("4.Pop Element from stack")
    print("5.Delete the stack")
    print("6.Peek element from stack")
    print("7.Exit")

    choice=int(input("Enter your choice: "))
    if choice==1:
        val=int(input("Enter the value for stack: "))
        stackobj.push(val)
    elif choice==2:
        stackobj.displaystack()
    elif choice==3:
        print(stackobj.isEmpty())
    elif choice==4:
        print(stackobj.pop())
    elif choice==5:
        print(stackobj.deletestack())
    elif choice==6:
        print(stackobj.peek())
    elif choice==7:
        sys.exit()
    else:
        print("Invalid choice")