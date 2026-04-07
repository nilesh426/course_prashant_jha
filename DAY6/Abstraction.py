# Abstraction: It is a process of hiding the internal details and showing only the necessary details to the user.
# Python does not support abstraction it needs abc module to be imported
# from abc import ABC, abstractmethod
# class Help4code(ABC):
#     @abstractmethod
#     def training(self):
#         pass
#     def placement(self):
#         pass

# class Ashish(Help4code):
#     def training(self):
#         print("C,C++,Java")
#     def placement(self):
#         print("Java placement")

# class Ankush(Help4code):
#     def training(self):
#         print("Python , Django")
#     def placement(self):
#         print("Python placement")

# class Prashant(Help4code):
#     def training(self):
#         print("Machine Learning")
#     def placement(self):
#         print("Data Science")

# obj1=Ashish()
# obj1.training()
# obj1.placement()

# obj2=Ankush()
# obj2.training()
# obj2.placement()

# obj3=Prashant()
# obj3.training()
# obj3.placement()

# from abc import ABC, abstractmethod
# class IRCTC(ABC):
#     @abstractmethod
#     def bookticket(self):
#         pass

# class MakeMyTrip(IRCTC):
#     def bookticket(self):
#         print("==================================")
#         print("           Welcome to MMT          ")
#         source = input("Enter source:")
#         destination = input("Enter destination:")
#         date = input("Enter date:")
#         print("==================================")
   

# class Goibibo(IRCTC):
#     def bookticket(self):
#         print("==================================")
#         print("           Welcome to Goibibo          ")
#         source = input("Enter source:")
#         destination = input("Enter destination:")
#         date = input("Enter date:")
#         print("==================================")

# class RedBus(IRCTC):
#     def bookticket(self):
#         print("==================================")
#         print("           Welcome to RedBus          ")
#         source = input("Enter source:")
#         destination = input("Enter destination:")
#         date = input("Enter date:")
#         print("==================================")

# obj1=MakeMyTrip()
# obj1.bookticket()

# obj2=Goibibo()
# obj2.bookticket()

# obj3=RedBus()
# obj3.bookticket()