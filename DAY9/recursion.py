#Recursion uses stack memory
#Recursion : We use recursion especially in the cases we know that a problem can be divided into smaller sub problems.
#Recursion is a process of calling the same function again and again.
# POINTS                      RECURSION      ITERATION              REASON
# Space Efficient?              NO              YES         No stack memory require in case of iteration 


# Time Efficient?               NO              YES         In case of recursion system needs more time 
#                                                           for pop and push elements to stack memory which 
#                                                           makes recursion less time efficient


# Easy to code?                  YES             NO          we use recursion especially in the cases we know that 
#                                                            a problem can be divided into similar sub problems

# Power of 2
# def powerofTwo(n):
#     if n==0:
#         return 1
#     else:
#         return 2*powerofTwo(n-1)
# print(powerofTwo(4)) #n=4

#Factorial
# def factorial(num):
#     if num<=1:
#         return 1
#     else:
#         return num*factorial(num-1)
# print(factorial(4))

#isPalindrome
# def ispalindrome(strng):
#     if len(strng)== 0:
#         return True
#     if strng[0] != strng[len(strng)-1]:
#         return False
#     return ispalindrome(strng[1:-1])

# print(ispalindrome("tacocat"))

#Bse and Power 
# def power(base , exponent):
#     if exponent==0:
#         return 1
#     else:
#         return base*power(base,exponent-1)

# print(power(2,0))
# print(power(2,2))
# print(power(2,4))
# print(power(2,6))

#capitalizeFirst
# def capitalizeFirst(arr):

#     result=[]
#     if len(arr)==0:
#         return result
    
#     result.append(arr[0][0].upper()+arr[0][1:])
#     return result+capitalizeFirst(arr[1:])

# print(capitalizeFirst(["car","taco","banana"])) 

#Product of Array
# def productofArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0]*productofArray(arr[1:])

# print(productofArray([1,2,3])) #6
# print(productofArray([1,2,3,10])) #60
# print(productofArray([])) #1

#Fibonacci solution
# def fib(num):
#     if(num<2):
#         return num
#     else:
#         return fib(num-1)+fib(num-2)
    
# print(fib(4)) #1,1,2,3,5,8,13,21,34,55,89,144