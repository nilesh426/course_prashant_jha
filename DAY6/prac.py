#WAP to compress a string by replacing consecutive characters with their counts
# s = "aaabbbccc"                    
# a = ""
# for i in s:
#     if i not in a:
#         a += i
#         a += str(s.count(i))
# print(s)
# print(a)

#WAP to reverse each word of string
# s="Hello World"
# a=s.split()
# print(a)
# for i in a:
#     print(i[::-1],end=" ")

#WAP to arraange the elements such that even numbers are in front and odd numbers are in back
n=int(input("Enter the size of list:"))
a=[]
b=[]
c=[]
d=[]
for i in range(n):
    b=int(input("Enter the number:"))
    a.append(b)
print(a)
for i in a:
    if i%2==0:
        c.append(i)
    else:
        d.append(i)
print("Odd=",d)
print("Even=",c)
list=c+d
print("Sorted list=",list)

        
        
   