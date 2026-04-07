#Encapsulation: It is process of protecting the data and functionality in a single unit.

# class Base: #parent class
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a="prashant" #public data member
#         self.__c="Ashish" #private data member
# #Creating a derived/child class
# class Derived(Base):#child class
#     def __init__(self):
#         # calling constructor of base class
#         Base.__init__(self)
#         #print("calling private member of base class")
#         # print(self.a)
#         # print(self.__c)

# # obj1=Derived()
# # print(obj1.a)
# # print(obj1.__c)
# obj2=Base()
# print(obj2.a) #Accessible
# print(obj2.__c) #Not accessible:Only accessible in class itself (private data member)
    

class Rbi:
    #Declaring public method
    def publicpolicy(self):
        print("check the public policy of RBI")
    
    #Declaring private method
    def __privatepolicy(self):
        print("There is some private policy not accessible for public")

class Sbi(Rbi):
    def __init__(self): #first sbi class const called
       Rbi.__init__(self) #second rbi class const called
    
    def callingPublicMethod(self): #child class public method
        print("\nInside child class")
        self.publicpolicy() #callling parent class public method

    def callingPrivateMethod(self): #child class private method
        self.__privatepolicy() #calling parent class private method

# obj1=Sbi()
# obj1.callingPublicMethod()
# obj1.callingPrivateMethod()
# obj1.publicpolicy()
# obj1.__privatepolicy()
# obj2=Rbi()
# obj2.publicpolicy()
# obj2.__privatepolicy()
# obj2=Rbi()
# obj2.publicpolicy()
# obj2._Rbi__privatepolicy() 