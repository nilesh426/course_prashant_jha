#Inheritance:Extends the properties of one class to another class
#Base class:A class which inherits to property to another is called base class or parent class.
#Derived class:A class in which properties are inherited is called derived class or child class.
#Types:1.Single Inheritance
       #2.Multiple Inheritance
       #3.Multilevel Inheritance


# 1.Single Inheritance
#syntax: class derived_class_name(base_class_name):
            #  ------------------------
            #  ------------------------

# class College:
#     def college_name(self):
#         print("College Name: YBIT")


# class student_info(College):
#     def student_info(self):
#         print("Name: Prashant Jha")
#         print("Roll No: 101")
#         print("Mobile No: 8767277605")
#         print("Address: Dhamtari, Chhattisgarh")
#         print("Branch: CE")

# obj= student_info()
# obj.college_name()
# obj.student_info()

# 2.Multilevel Inheritance
# Multilevel inheritance  
# class College:   #first class  first- level  
#   def college_name(self):  
#     print("     YBIT")  

# class Student(College): #second class second - level  
#   def student_info(self):  
#     print("Name:   Nilesh Sawant")  
#     print("Branch: Computer")  
  
# class Exam(Student): #child class  
#   def subject(self):  
#     print("Subject1: Design Engineering")  
#     print("Subject2: Math")  
#     print("Subject3: C-Language")  
# obj = Exam()  
# obj.college_name()  
# obj.student_info()  
# obj.subject()

# 3.Multiple Inheritance
# syntax : class derived_class_name(base_class_name1,base_class_name2):
            #  ------------------------
            #  ------------------------

class Submarks:
    math=int(input("Enter math marks:"))
    physics=int(input("Enter physics marks:"))
    chemistry=int(input("Enter chemistry marks:"))
    english=int(input("Enter english marks:"))
class Pracmarks:
    cpract=int(input("Enter cpract marks:"))

class result(Submarks,Pracmarks):
    # print("if student pass in both subject and paper then pass")
    def total(self):
        if self.math>=40 and self.physics>=40 and self.chemistry>=40 and self.english>=40 and self.cpract>=20:
            print("student is pass")
        else:
            print("student is fail")
obj=result()
obj.total()
   