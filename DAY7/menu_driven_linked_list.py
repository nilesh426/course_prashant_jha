
import sys

class Node:
    def __init__(self,data):
        self.data= data #instance variable
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def addnode(self,value):
        node=Node(value)
        if self.head==None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
    
    def addnodebeginning(self,value):
        node = Node(value)
        if self.head == None:
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head=node

    def addnodebetween(self,index,value):
        node = Node(value)
        if self.head == None:
            self.head=node
            self.tail=node
        elif index==0:
            node.next = self.head
            self.head=node
        else:
            temp=self.head
            for _ in range(index-1):
                temp=temp.next
            node.next=temp.next
            temp.next=node

    def deletenode(self,index):
        if index==0:
            self.head=self.head.next
        else:
            temp=self.head
            for _ in range(index-1):
                temp=temp.next
            temp.next=temp.next.next

    def searchnode(self,value):
        temp=self.head
        while temp!=None:
            if temp.data==value:
                return True
            temp=temp.next
       
    def displaylinkedlist(self):
        temp=self.head
        while temp!=None:
            print("!",temp.data,"!-->",end="")
            temp=temp.next
            
            
if __name__ == '__main__':
    object=Linkedlist()

    while True:
        print()
        print("Menu Driven Linkedlist")
        print("1.Add node Linkedlist")
        print("2.Add Node in Beginning")
        print("3.Add Node in Between")
        print("4.Display Linkedlist")
        print("5.Delete Node")
        print("6.Search Node")
        print("7.Exit")

        choice=int(input("Enter your choice:"))
        if choice==1:
            value = int(input("Enter the value for node: "))
            object.addnode(value)
            print("Node added successfully in single linkedlist.")
        elif choice==2:
            value=int(input("Enter the value for node: "))
            object.addnodebeginning(value)
            print("Node added at the beginning")
        elif choice==3:
            value=int(input("Enter the value for node: "))
            index=int(input("Enter the index: "))
            object.addnodebetween(index,value)
            print("Node added in between")
        elif choice==4:
            print("Elements in the linkedlist are:")
            object.displaylinkedlist()
        elif choice==5:
            index=int(input("Enter the index: "))
            object.deletenode(index)
            print("Node",index," deleted successfully")
        elif choice==6:
            value=int(input("Enter the value for node: "))
            if object.searchnode(value):
                print("Node found")
            else:
                print("Node not found")


        elif choice==7:
            sys.exit()
            print("Exiting...") 
        else:
            print("Invalid choice")
   