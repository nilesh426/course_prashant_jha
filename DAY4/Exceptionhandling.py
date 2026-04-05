#Exception handling : Exception handling is a process to handle the error that occurs during the execution of a program.
# n1 = int(input("Enter the value of n1: "))
# n2 = int(input("Enter the value of n2: "))
# try:
#     print(n1/n2)
# except:
#     print("Cannot divide by zero")

# print("To be continue")

#multiple except block
# try:
#     n1 = int(input("Enter the value of n1: "))
#     n2 = int(input("Enter the value of n2: "))
#     print(n1/n2)
# except ZeroDivisionError:
#     print("Cannot divide by zero")
# except ValueError:
#     print("Enter only integer value")

# print("To be continue")

#single except block for handling different types of exception
# try:
#     n1=int(input("Enter value of n1:"))
#     n2=int(input("Enter value of n2:"))
#     print(n1/n2)
# except (ZeroDivisionError,ValueError) as message:
#     print(message)

#The concept of default except block
# try:
#     n1=int(input("Enter value of n1:"))
#     n2=int(input("Enter value of n2:"))
#     print(n1/n2)

# except (ZeroDivisionError,ValueError) as message:
#     print(message)
# except:
#     print("This is default part of except block")

#else in exception
# try:
#     n1=int(input("Enter value of n1:"))
#     n2=int(input("Enter value of n2:"))
#     print(n1/n2)
# except (ZeroDivisionError,ValueError) as message:
#     print("Enter correct number:",message)
# else:
#     print("Everything is ok")

#finally in exception
# try:
#     n1=int(input("Enter value of n1:"))
#     n2=int(input("Enter value of n2:"))
#     print(n1/n2)
# except (ZeroDivisionError,ValueError) as message:
#     print("Enter correct number:",message)
# finally:
#     print("I will always execute")

#nested try except block
# try:
#     n1=int(input("Enter value of n1:"))
#     n2=int(input("Enter value of n2:"))
#     try:
#         print(n1/n2)
#     except ZeroDivisionError as msg:
#         print(msg)
# except ValueError as msg:
#     print(msg)

#nested try except  finally block
# try:
#     n1=int(input("Enter value of n1:"))
#     n2=int(input("Enter value of n2:"))
#     print(n1/n2)
# except (ZeroDivisionError,ValueError) as msg:
#         print(msg)
# else:
#         print("Everything is ok")
# finally:
#       print("I will always execute")



#