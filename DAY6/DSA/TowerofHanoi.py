# import time

# class TowerOfHanoi:
#     def __init__(self, source):
#         self.rod_A = source[:]
#         self.rod_B = []
#         # self.rod_C = []
#         self.total_disks = len(source)

#     def show_rods(self):
#         print(f"A = {str(self.rod_A):<12} B = {str(self.rod_B):<12} C = {str(self.rod_C):<12}")
#         print("-" * 45)
#         time.sleep(1)

#     def move_between_rods(self, from_rod, to_rod):
#         if not from_rod:
#             from_rod.append(to_rod.pop())
#         elif not to_rod:
#             to_rod.append(from_rod.pop())
#         elif from_rod[-1] > to_rod[-1]:
#             from_rod.append(to_rod.pop())
#         else:
#             to_rod.append(from_rod.pop())

#         self.show_rods()

#     def solve_iteratively(self):
#         self.show_rods()  # initial state

#         # Decide movement pattern
#         if self.total_disks % 2 == 0:
#             move1 = (self.rod_A, self.rod_B)
#             move2 = (self.rod_A, self.rod_C)
#             move3 = (self.rod_B, self.rod_C)
#         else:
#             move1 = (self.rod_A, self.rod_C)
#             move2 = (self.rod_A, self.rod_B)
#             move3 = (self.rod_B, self.rod_C)

#         total_moves = 2 ** self.total_disks - 1

#         for step in range(1, total_moves + 1):
#             if step % 3 == 1:
#                 self.move_between_rods(*move1)
#             elif step % 3 == 2:
#                 self.move_between_rods(*move2)
#             else:
#                 self.move_between_rods(*move3)


# # Run
# hanoi = TowerOfHanoi([3, 2, 1])
# hanoi.solve_iteratively()

import time
class Tower:
    def __init__(self, source):
        print("Welcome to Tower of Hanoi Game!")
        print()
        print("Given Problem     A=[3, 2, 1]   B=[]   C=[]")
        print()
        print("Expected Output   A=[]   B=[]   C=[3, 2, 1]")
        self.A = []   
        self.B = []         
        self.C = []          

    def tower(self,item):
        self.A.append(item)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A)
        print("Items in Tower A\n" )

    def pass1(self):
        self.temp = self.A.pop()
        self.C.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass One Completed==========================" )

    def pass2(self):
        self.temp = self.A.pop()
        self.B.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Two Completed==========================" )

    def pass3(self):
        self.temp = self.C.pop()
        self.B.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Three Completed==========================" )

    def pass4(self):
        self.temp = self.A.pop()
        self.C.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Four Completed==========================" )

    def pass5(self):
        self.temp = self.B.pop()
        self.A.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Five Completed==========================" )

    def pass6(self):
        self.temp = self.B.pop()
        self.C.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Six Completed==========================" )

    def pass7(self):
        self.temp = self.A.pop()
        self.C.append(self.temp)
        time.sleep(1)  # delay (1 second)
        print("A=",self.A  ,"   ",    "B=",self.B  ,"   ",    "C=",self.C)
        print("Pass Seven Completed==========================" )
    
obj = Tower([3,2,1])
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()
    
    
    
    
    


    
       
       
        