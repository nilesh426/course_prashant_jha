# for i in range(5,0,-1):
#     print(i)

# for i in range(10,0,-2):
#     print(i)

#wap to reverse the string
# name = "Mumbai"
# result = ""
# n=len(name)
# for i in range(n-1,-1,-1):
#     result +=  name[i]
# print(name) #Mumbai
# print(result) #iabmuM

#WAP to check whether the string is palindrome or not
name = input("Enter a string: ")
print("String=",name) #tnawashselin
result = name[::-1] 
if(name == result):
    print(" It is a palindrome")
else:
    print(" It is not a palindrome")