class Node:
    def __init__(self,data):
        self.data= data #instance variable
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

linkedlist=Linkedlist()
linkedlist.head=Node(5) #first node
second         =Node(10)
third          =Node(15)
fourth         =Node(20)

#linking part
linkedlist.head.next=second
second.next=third
third.next=fourth

print(linkedlist.head.data)
print(second.data)
print(third.data)
print(fourth.data)

print(linkedlist.head.next)
print(second.next)
print(third.next)
print(fourth.next)
#display linkedlist
while linkedlist.head!=None:
    print("!",linkedlist.head.data,"!",linkedlist.head.next,"-->",end=" ")
    linkedlist.head = linkedlist.head.next