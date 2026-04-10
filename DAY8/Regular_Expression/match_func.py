# import re
# a=input("Enter string to perform match operation:")
# mtch=re.match(a,"python is a very important language")
# print(mtch)
# if mtch!=None:
#     print("match found at the beginning level")
#     print(mtch.start(),"...",mtch.end())
# else:
#     print("there is no matching at beginning level")
#Output:
#Enter string to perform match operation:python
# <re.Match object; span=(0, 6), match='python'>
# match found at the beginning level
# 0 ... 6 

import re
a=input("Enter the string:")
f=open("myfile.txt","r")
c=f.read()
mtch= re.search(a,c)
print(mtch)
if mtch!=None:
    print("match found at the beginning level")
    print(mtch.start(),"...",mtch.end())
else:
    print("there is no matching at beginning level")

#Output
# Enter the string:matrix
# <re.Match object; span=(13, 19), match='matrix'>
# match found at the beginning level
# 13 ... 19