# mydict= {
#     101:"Nilesh",
#     102:"Sawant",
#     "103":"mohini",
#     "104":"trivani",
#     101:"ashish",    #updates the value of the key if key is already present
#     104:"ashish"
# }
# # print(mydict)
# mydict.pop(101)
# print(mydict)

#with the help of key we have to print the value
# a = mydict["103"]
# print(a)

#we will replace old value by new value
# mydict["103"] = "peter"
# print(mydict)

#if we have to only print the keys
# for x in mydict:
#     print(x)

#if we have to only print the values
# for x in mydict.values():
#     print(x)

#if we have to only print the keys and values
# for x,y in mydict.items():
#      print(x,y)

#if we want to add new key and value pair
# mydict["mobile_no"]=46464646
# print(mydict)

# a= {(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5]) #3

# a={'a':1,'b':2,'c':3}
# print(a['a','b']) #key error

# arr={}
# arr[1]=1
# arr['1']=2
# arr[1] += 1
# sum =0
# for k in arr:
#     sum += arr[k]
# print(sum)  #4

# mydict={}
# mydict[1]=1
# mydict['1']=2
# mydict[1.0]=4
# sum=0
# for k in mydict:
#     sum += mydict[k]
# print(sum) #6

# mydict={}
# mydict[(1,2,4)]=8
# mydict[(4,2,1)]=10
# mydict[(1,2)]=12
# sum=0
# for k in mydict:
#      sum += mydict[k]
# print(sum)
# print(mydict) #{(1, 2, 4): 8, (4, 2, 1): 10, (1, 2): 12} =30

# box={}
# jars={}
# crates={}
# box['biscuit']=1
# box['cake']=3
# jars['jam']=4
# crates['box']=box
# crates['jars']=jars
# print(len(crates(box))) #TypeError: len() of unsized object

# dict={'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_])

# rec = {
#     "name":"Prashant",
#     "age":25,
#     "gender":"male"
# }
# r=rec.copy()
# print(id(r)==id(rec)) #False
# print(rec)
# print(id(r))
# print(id(rec)) 

# rec={"Name":"Python","Age":25,"Gender":"Male"}
# id1=id(rec)
# print(id1)
# del rec
# rec={"Name":"Python","Age":25,"Gender":"Male"}
# id2=id(rec)
# print(id2)
# print(id1==id2)

#wap to find the minimum value in the dictionary
# a={"x":20,"y":10,"z":40}
# for i,j in a.items():
#     if j==min(a.values()):
#         print(i)


    