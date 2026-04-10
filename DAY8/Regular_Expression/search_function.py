import re
a=input("Enter string to perform match operation:")
mtch=re.search(a,"python is a very important language")
print(mtch)
if mtch!=None:
    print("match found")
    print(mtch.start(),"...",mtch.end())
else:
    print("there is no matching anywhere")
    
#Output:
# Enter string to perform match operation:language
# <re.Match object; span=(27, 35), match='language'>
# match found
# 27 ... 35