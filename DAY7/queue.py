# Data structures are diiferent ways of organizing data in a computer memory that can be used effectively.

#Queue implementation with size limit
import sys
class Queue():
    def __init__(self, queueSize):
        self.queuelist=[]
        self.queueSize= queueSize
        
    def isFull(self):
        if len(self.queuelist) ==self.queueSize:
            return True
        else:
            return False
        
    def Enqueue(self,value):
        if self.isFull():
            print("queue is Full")
        else:
            self.queuelist.append(value)
        
        
    def displayQueue(self):
        print("------====-----====-----=====-----====-----")
        print(self.queuelist)
        print("------====-----====-----=====-----====-----")
        print()
    def isEmpty(self):
        if self.queuelist==[]:
            return True
        else:
            return False
    def Dequeue(self):
        if self.isEmpty():
            return "queue is empty"
        else:
            return self.queuelist.pop(0)      
          
    def deleteQueue(self):
        self.queuelist= []  
        return "Queue is deleted" 
    
    def peekQueue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.queuelist[0]  
            
size = int(input("Enter the size of queue:"))
queueObj=Queue(size)         #
while True:
    
    print("1. Enqueue Element in Queue")
    print("2. Display queue element")
    print("3. Check Queue is empty")
    print("4. Dequeue elements from queue")
    print("5. Delete queue")
    print("6. Peek")
    print("7. Exit")
    
    choice =int(input("Enter your choice: "))
    print()
    if choice == 1:
        val=int(input("Enter value for queue: "))
        queueObj.Enqueue(val)
    elif choice==2:
        queueObj.displayQueue()    
    elif choice==3:
        print(queueObj.isEmpty())   
        print() 
    elif choice==4:
        print("Dequeued element is :",queueObj.Dequeue())   
        print() 
    elif choice==5:
        queueObj.deleteQueue()  
    elif choice==6:
        print("The peek element is :",queueObj.peekQueue()) 
        print()   
    elif choice==7:
        sys.exit()    
    else:
        print("Enter Right Choice")    
        print()