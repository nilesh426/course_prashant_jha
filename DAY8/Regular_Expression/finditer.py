# import re
# count=0
# matcher=re.finditer("Hi","HiHiHiHi")
# for i in matcher:
#     count+=1
#     print(i.start(),"...",i.end(),"...",i.group())
# print("The number of occurences:",count)

#Output:
# 0 ... 2 ... Hi
# 2 ... 4 ... Hi
# 4 ... 6 ... Hi
# 6 ... 8 ... Hi
# # The number of occurences: 4

# import re
# obj=input("Enter the string:")
# objmatch=re.finditer(obj,"a7b @k9z")
# for match in objmatch:
#     print(match.start(),".....",match.end(),".....",match.group())



