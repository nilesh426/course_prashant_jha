# rows = int(input("Enter number of rows: "))
# cols = int(input("Enter number of columns: "))
# a=[]
# matrix = []

# for i in range(rows):
#     row = list(map(int, input(f"Enter row {i+1} elements: ").split()))
#     a.append(max(row))
#     matrix.append(row)

# print("Matrix is:")
# for r in matrix:
#     print(r)
    
# print()
# print(a)

#WAP to remove only leading zeros from a list of integers using for loop
s = [0,1,0,2,4,3,0,7,0,5]
result = []
started = False

for num in s:
    if num != 0:
        started = True
    if started:
        result.append(num)

print(s)
print(result)