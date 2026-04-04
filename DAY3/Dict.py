# mydict= {
#     101:"Nilesh",
#     102:"Sawant",
#     "103":"mohini",
#     "104":"trivani",
#     101:"ashish",    #updates the value of the key if key is already present
#     104:"ashish"
# }
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

arr={}
arr[1]=1
arr['1']=2
arr[1] += 1
sum =0
for k in arr:
    sum += arr[k]
print(sum)