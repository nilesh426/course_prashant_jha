# import re
# mo = input("Enter the number:")
# obj=re.fullmatch("[0-9]\d{9}",mo)
# if obj!=None:
#     print("valid number")
# else:
#     print("invalid number")

# import re
# s = input("Enter the email:")
# obj=re.fullmatch("\w[a-zA-Z0-9_.]*@gmail.com",s)
# if obj!=None:
#     print("valid Email ID")
# else:
#     print("Invalid Email ID")

import os,sys
fname=input("Enter the file name:")
if os.path.isfile(fname):
    print("File exists:",fname)
    f=open(fname,"r")
else:
    print(fname,"is not a file")
    sys.exit(0)
print("The content of the file is:")
data=f.read()
print(data)