# num=123

# a=num%10  #3
# num=num//10  #12
# b= num%10  #2
# c=num//10 #1
# rev=a*100+b*10+c
# print(rev)

num=123456

a=num%10  #6
num=num//10 #12345
b=num%10  #5
num=num//10 #1234       
c=num%10  #4
num=num//10 #123
d=num%10  #3
num=num//10 #12
e=num%10  #2
f=num//10 #1
rev=a*100000+b*10000+c*1000+d*100+e*10+f
print(rev)

