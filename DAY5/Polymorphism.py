#Polymorphism: same function name but different functionality
#Polymorphism Example
class Principal:
    def role(self):
        print("Principal role")
    
class Dean:
    def role(self):
        print("Dean role")

class Hod:
    def role(self):
        print("Hod role")

class Teacher:
    def role(self):
        print("Teacher role")

#===========class declaration completed==============#
def func(obj):
    obj.role()

campus=[Principal(),Dean(),Hod(),Teacher()]
for obj in campus:
    func(obj)