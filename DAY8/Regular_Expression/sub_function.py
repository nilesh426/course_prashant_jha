
# import re
# mtch = re.sub("[a-zA-Z]","*","2345 fabc ABCD deff")
# print(mtch)


import re
a=input("Enter the string:")
mtch = re.sub("[0-6]","*",a)
print(mtch)