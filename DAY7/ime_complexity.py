
# def Findbiggestnumber(Array):       #====================>O(1) 
#     firstvalue = Array[0]           #======>O(1) \
#                                                 # \
#     for i in range(1,len(Array)):   #======>O(n)  /=======>O(n)     O(1)+O(n)+O(1)=O(n)
#         if Array[i] > firstvalue:   #======>O(1) /
#             firstvalue = Array[i]   #======>O(1)
#     return firstvalue               #====================>O(1)

# Array = [1,2,3,4,5,6,99,8,9,10]
# print(Findbiggestnumber(Array))


#========linear search===========# Final time complexity = O(n)
# def linearsearch(array,target):
#     for i in range(len(array)):
#         if array[i]==target:
#             return i
#     return -1

# array=[1,2,3,4,5,6,7,8]           
# target=55
# result=linearsearch(array,target)
# if result==-1:
#     print("Element not found")
# else:
#     print("Element found at index=",result)

#===============Binary Search===============#
def binarysearch(array,target):
   start=0
   end=len(array)-1 #8
   while start<=end:
       mid = (start+end)//2
       if mid==target:
           return mid
       elif target>mid:
           start=mid+1
       else:
           end=mid-1
   return -1

sortedarray=[1,2,3,4,5,6,7,8]           
target=55
result=binarysearch(sortedarray,target)
if result==-1:
    print("Element not found")
else:
    print("Element found at index=",result)