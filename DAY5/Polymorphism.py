#Polymorphism: same function name but different functionality
#Polymorphism Example
# class Principal:
#     def role(self):
#         print("Principal role")
    
# class Dean:
#     def role(self):
#         print("Dean role")

# class Hod:
#     def role(self):
#         print("Hod role")

# class Teacher:
#     def role(self):
#         print("Teacher role")

# #===========class declaration completed==============#

# def func(obj):
#     obj.role()

# campus=[Principal(),Dean(),Hod(),Teacher()]
# for obj in campus:
#     func(obj)


#============================OVERLOADING==============================#
#Overloading:Python does not support method and constructor overloading
# class Arithmetic:
#     def add(self,a):
#         print(a)

#     def add(self,a,b):
#         print(a+b)

#     def add(self,a,b,c):
#         print(a+b+c)

# a=Arithmetic()
# a.add(10)
# a.add(10,20)
# a.add(1,2,3)

# class Arithmetic:
#     def add(self,a=None,b=None,c=None):
#         if a!=None and b!=None and c!=None:
#             print(a+b+c)
#         elif a!=None and b!=None:
#             print(a+b)
#         else:
#             print("enter atleast two argument")

# a=Arithmetic()
# a.add(10)
# a.add(10,20)
# a.add(1,2,3)

# class Arithmetic:
#     def __init__(self):
#         print("There is no argument")
#     def __init__(self):
#         print("There is one argument")
#     def __init__(self):
#         print("There are two argument")

# obj=Arithmetic()
# obj=Arithmetic(10)
# obj=Arithmetic(2,2)

#============================OVERRIDING==============================#
#Overriding:Same function name but different functionality
# class Rbi:
#     def home_loan(self):
#         print("Home Loan=7.5")
#     def carloan(self):
#         print("car loan=8")
    
# class Sbi:
#     def home_loan(self):
#         print("Home Loan=8.5")
#     def car_loan(self):
#         print("car loan=9")

# obj=Sbi()
# obj.home_loan()
# obj.car_loan()

#Using super() to access 
class Rbi:
    def home_loan(self):
        print("Home loan interest rate is 7%")
    def car_loan(self):
        print("Car loan interest rate is 8%")
        
        
class Sbi(Rbi):
    def home_loan(self):
        print("Sbi Provide home loan at 6 interest rate")
    def car_loan(self):
        print("Car loan interest rate is 7")
        super().home_loan() 
        super().car_loan()  #calling method of parent class using super() function
        
obj = Sbi()   #creating object of child class
obj.home_loan()   #calling method of child class using child
obj.car_loan()    #calling method of child class using child



#constructor overriding
# class Father:
#     def __init__(self):
#         print("Father := i am already at breakfast table")

# class Child(Father):
#     def __init__(self):
#         print("Child := i will be late for breakfast")
#         super().__init__()

# obj=Child()
