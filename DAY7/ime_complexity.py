
def Findbiggestnumber(Array):       #====================>O(1) 
    firstvalue = Array[0]           #======>O(1) \
    for i in range(1,len(Array)):   #======>O(n)  =======>O(n)     O(1)+O(n)+O(1)=O(n)
        if Array[i] > firstvalue:   #======>O(1) /
            firstvalue = Array[i]   #======>O(1)
    return firstvalue               #====================>O(1)

Array = [1,2,3,4,5,6,99,8,9,10]
print(Findbiggestnumber(Array))