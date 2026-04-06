#object Oriented Programming: Abstraction, Encapsulation, Inheritance, Polymorphism : 4 pillars of OOPs
#first letter of class name should be capital
#self: It is a reference variable which is used to refer the current object
# construct:we initialize the object of the class
#constructor is called only one time for one object because memory is allocated only once
#Python has a default constructor which is called when an object is created if we have not used a constructor in the program
# class Student:

#     roll_no=101 #data member

#     def student_data(self): #member function/method
#         print("Student Information")

# obj=Student() #self:reference variable
# print(obj.roll_no) #accessing data member
# obj.student_data() #accessing member function

# class Demo:
#     def __init__(self): parametrized constructor
#      print("I am constructor")

#     def msg(self):
#         print("Hello World!")

# obj1=Demo()
# # print(obj1)
# obj2=Demo()
# obj1.msg()

# class Hod:
#     def __init__(self): #constructor
#         self.name="Prashant jha"
#         self.age=26
#         self.empid=1007
#     def info(self): #instance method
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Empid:",self.empid)
# obj1=Hod() #object created
# obj1.info()

# class Hod:
#     def __init__(self,name,age,rollno): #constructor
#         self.name=name
#         self.age=age
#         self.rollno=rollno
#     def info(self): #instance method
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Rollno:",self.rollno)
# obj1=Hod("Arjun",45,101) #object created
# obj1.info()

# class New:
#     def __init__(self):
#         self.a=10

# obj1=New()
# obj2=New()
# obj3=New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# obj1.a=20  #instance variable is dependent on the object , change to one object do not reflect to another object
# print()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)

#where we can declare the instance variable
# class Student:
#     def __init__(self):
#         self.s_name="Prashant"
#         self.s_rollno=101  #declaring instance variable inside a constructor

#     def getdata(self):
#         self.s_mb = 8787878787 #declaring a instance var inside a instance method

# obj=Student()
# obj.getdata()
# del obj.s_name     #deleting instance variable using object
# obj.s_branch="CE"  #adding a new instance variable using object
# print(obj.__dict__)

#Static Variable
# static variable is dependent on class
# class New:
#     a=10
#     def __init__(self):
#         self.name="Nilesh"

# obj1=New()
# obj2=New()
# obj3=New()
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)
# New.a=50
# print(obj1.a)
# print(obj2.a)
# print(obj3.a)