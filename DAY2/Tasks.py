# names = [4,2,5,6,8,2]
# for i in names:
#     print(i)

#WAP to move all the zeroes in the list to the end of the list
# A=[4,0,2,5,0,1]
# for i in A:
#     if i==0:
#         A.remove(i)
#         A.append(i)
# print(A) #[4, 2, 5, 1, 0, 0]

# WAP to remove duplicates from the list
# L=[1,2,2,3,3,4,4,5]
# a=[]
# for i in L:
#     if i not in a:
#         a.append(i)
# print(L)
# print(a) #[1, 2, 3, 4, 5]


#WAP to find the common elements in three lists
#  a=[1,2,3]
# b=[2,3,4]
# c=[3,4,5]
# for i in (a):
#     if i in b and i in c:
#         print(i)

#WAP to find distance between ajacent elements and return the sum of those distances
# n = int(input("Enter size of array:"))
# arr=[]
# for i in range(n):
#     val = int(input("Enter element:"))
#     arr.append(val)
# sum=0
# print(arr)
# for i in range(n):
#     if i+1 in range(n):
#         sum+= abs(arr[i]-arr[i+1])
# print(sum)

# for i in range(1,5):
#      if i==3:
#         break
#      print(i)

# for i in range(1,5):
#      if i==3:
#         continue
#      print(i)

# for i in range(1,5):
#      if i==3:
#         break
#      print(i)


#zip() we can take multiple range in same loop
# for i,j in zip(range(1,6),range(5,0,-1)):
#      if i==3:
#         continue
#      print(i,"  ",j)

# for i,j in zip(range(1,7),range(6,0,-1)):
#         if i==3 and j==3:
#              continue
#         print(i,"  ",j)


# a = "prashant*is*a*good*programmer"
# newstr=""
# for i in a:
#     if i!="*":
#         newstr = newstr + i
#     else:
#         newstr = i + newstr
# print(newstr) #***prashantisagoodprogrammer

#BODMAS
# A=50
# B=30
# C=20
# D=10

# print((A+B)*C/D) 
# print((A-B)*(C/D))
# print(A+(B*C)/D)

# X=['A','B','C']
# Y=['A','B','C']
# Z=[1,2,3,4]
# print(id(X)) 
# print(id(Y)) 
# print(X==Y) #True
# print(X==Z) #False
# print(X != Z) #True

#WAP to check whether the given string is anagram or not
# a="silent"
# b="listen"
# if len(a)==len(b):
#     for i in a:
#         if i not in b:
#             print("Not Anagram")
#             break
#     else:
#         print("Anagram")

#WAP to count the number of words in a string
# a = "Hello World Python Programming"
# word=1
# for i in a:
#     if i==" ":
#         word += 1
# print(word ) 

#wap to return an array where each element is product of other elements
a=[1,2,3,4,5]
b=[]
for i in range(len(a)):
    for j in range(len(a)):
        if i!=j:
            b.append(a[i]*a[j])
print(b)



