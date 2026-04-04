#(i,j)
# for i in range(1,4):
#     for j in range(1,4):
#         print(i , end=" ")  #end is used to print in same line with space
#     print() #for newline

# for i in range(1,n+1):
#     for j in range(1,i):
#         print(j , end=" ")  #end is used to print in same line with space
#     print() #for newline

# n=5
# for i in range(1,n+1):
#      for j in range(1,1+i):
#          print(chr(64+i), end=" ")  #end is used to print in same line with space
#      print() #for newline

# n=5
# for i in range(1,n+1):
#       for j in range(1,n+2-i):
#           print("*", end=" ")  #end is used to print in same line with space
#       print() #for newline

# n=5
# for i in range(1,n+1):
#       for j in range(1,n+2-i):
#           print(chr(64+j), end=" ")  #end is used to print in same line with space
#       print() #for newline

# import time
# n=5
# for i in range(1,n+1):
#       for j in range(1,n+2-i):
#           time.sleep(1)
#           print(n+1-i, end=" ")  #end is used to print in same line with space
#       print() #for newline

import time
n=10
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        time.sleep(2)
        print("*",end=" ")
    print()
