import re
a=input("Enter string to perform match operation:")
mtch=re.fullmatch(a,"pythonisvery")
print(mtch)
if mtch!=None:
    print("match found at the beginning level")
    print(mtch.start(),"...",mtch.end())
else:
    print("Full match not found")