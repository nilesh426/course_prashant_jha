mylist = ["prashant","ankush","ashish","satyarth","77","yash","nilesh"]

# print(mylist) #['prashant', 'ankush', 'ashish', 'satyarth', '77', 'yash', 'nilesh']
# print(type(mylist)) #<class 'list'>
# print(mylist[0]) #prashant
# print(mylist[1]) #ankush
# print(mylist[2]) #ashish
# print(mylist[-1]) #nilesh
# print(mylist[2:5]) #['ashish', 'satyarth', '77']
# print(mylist[:5]) #['prashant', 'ankush', 'ashish', 'satyarth', '77']
# print(mylist[1:]) #['ankush', 'ashish', 'satyarth']
# print(mylist[1:8:2]) #['ankush', 'satyarth', 'yash']
# print(mylist[:]) #['prashant', 'ankush', 'ashish', 'satyarth', '77', 'yash', 'nilesh']
# print(mylist[::-1]) #['nilesh', 'yash', '77', 'satyarth', 'ashish', 'ankush', 'prashant']

# mylist[2] = "mukesh"
# print(mylist) #['prashant', 'ankush', 'mukesh', 'satyarth', '77', 'yash', 'nilesh']

# if "prashant" in mylist:
#     print("yes")
# else:
# #     print("no")

# mylist.append('harsh')
# mylist.append('laxman')
# print(mylist) #['prashant', 'ankush', 'ashish', 'satyarth', '77', 'yash', 'nilesh', 'harsh', 'laxman']

# mylist.insert(1,"virat")
# print(mylist) #['prashant', 'ankush', 'ashish', 'satyarth', 'virat', '77', 'yash', 'nilesh', 'harsh', 'laxman']

# mylist.remove("nilesh")
# print(mylist) #['prashant', 'ankush', 'ashish', 'satyarth', 'virat', '77', 'yash', 'harsh', 'laxman']

# newlist = mylist.copy()
# print(newlist) #['prashant', 'ankush', 'ashish', 'satyarth', 'virat', '77', 'yash', 'harsh', 'laxman']

# mylist = [["prashant","jha"],
#           ["85.56","90.90"],
#           ["404040","505050"]]
# print("example of multidimensional list")
# print(mylist) #[['prashant', 'jha'], ['85.56', '90.90'], ['404040', '505050']]
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][1])
# print(mylist[0][0])

# list1 = ["nilesh","sawant"]
# print(list1*3)

# list2 = [1,2,3,4,5]
# print(list1+list2)

# list2 = [1,2,3,4,5]
# # del list2[1]
# # print(list2) #NameError: name 'list2' is not defined
# list2.clear()
# print(list2) #[]

# name = "nilesh"
# print(name)
# myname = list(name)
# print(myname) #['n', 'i', 'l', 'e', 's', 'h']

# mylist = [40,50,60,67]
# mylist.reverse()
# print(mylist) #[67, 60, 50, 40]

# list = [9,56,10,53,78,45]
# list.sort()
# print(list) #[9, 10, 45, 53, 56, 78] ascending oder

# list.sort(reverse=True)
# print(list) #[78, 56, 53, 45, 10, 9]  reverse=True-->descending order

# #Alising
# mylist = [44,55,66,77,88,99]
# newlist = mylist
# print(id(mylist))
# print(id(newlist)) 
# mylist[0]="append"
# print(mylist) #[44, 55, 66, 77, 88, 99]
# print(newlist) #[44, 55, 66, 77, 88,

# arr = [[1,2,3,4],
#        [4,5,6,7],
#        [7,8,9,10],
#        [11,12,13,14]]
# for i in range(0,4):
#     print(arr[i].pop())

arr=[1,2,3,4,5,6]
for i in range(1,6):
    arr[i-1]=arr[i]
for i in range(0,6):
    print(arr[i],end=" ")