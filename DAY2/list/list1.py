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

if "prashant" in mylist:
    print("yes")
else:
    print("no")
