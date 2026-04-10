import re
a=input("Enter the string:")
mtch = re.subn("[0-9]","*",a)
print(mtch)
print("The string is:",mtch[0])
print("The number of replacemnt is:",mtch[1])

#Output:
# Enter the string:wfuy3y383ifh3ufguf33fygfu4334f7ynfhf4
# ('wfuy*y***ifh*ufguf**fygfu****f*ynfhf*', 13)
# The string is: wfuy*y***ifh*ufguf**fygfu****f*ynfhf*
# The number of replacemnt is: 13

