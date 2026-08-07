# ====================================Problem 1 : Delivery Route Coordinate Finder ======================================================= #
# Delivery Route Coordinate Finder
# HARD
# A delivery company stores stop locations as (x, y) coordinate pairs. The dispatcher wants to find the stop that is farthest from the depot at (0, 0).
# Input Format
# Line 1: An integer n — the number of stops
# Next n lines: two space-separated integers x y for each stop
# Output Format
# Line 1: The coordinates of the farthest stop, space-separated

# Solution :

# def solve():
#     n = int(input())
    
#     max_dist = -1
#     ans_x , ans_y = 0 ,0
#     for i in range(n):
#         x , y = map(int , input().split())
#         dist = x*x + y*y

#         if dist > max_dist:
#             max_dist = dist
#             ans_x , ans_y = x , y
        
#     print(ans_x,ans_y)

# solve()


# =============================================Problem 2 : Inventory Tuple Counter ========================================================= #
# Inventory Tuple Counter
# EASY
# A warehouse logs each item scan during the day. A manager wants to know how many times a specific item code was scanned.
# Input Format
# Line 1: An integer n — the number of scan records
# Next n lines: one item code per line
# Final line: the item_code to search for
# Output Format
# Line 1: The number of times item_code was scanned

# Solution:

# def solve():
#      text = input().lower()
#      words = text.split()
#      freq = {}
#      
#      for word in words:
#          freq[word] = freq.get(word , 0)+1
#          
#      for word , count in freq.items():
#           print( word , count)
# 
# solve()

