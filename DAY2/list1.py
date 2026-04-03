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

list2 = [1,2,3,4,5]
# del list2[1]
# print(list2) #NameError: name 'list2' is not defined
list2.clear()
print(list2) #[]