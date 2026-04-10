class Tree:
    def __init__(self,value):
        self.value = value
        self.children = []
    
    def addChild(self,child):
        self.children.append(child)

    def __str__(self,level=0):     #It is used to print the tree structurefcc
        ret = "   " * level + str(self.value) + "\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret

rootnode=Tree("N1")
N2=Tree("N2")
N3=Tree("N3")
N4=Tree("N4")
N5=Tree("N5")
N6=Tree("N6")
N7=Tree("N7")
N9=Tree("N9")
N10=Tree("N10")


rootnode.addchild(N2)
rootnode.addchild(N3)


N2.addchild(N4)
N2.addchild(N5)
N3.addchild(N6)
N3.addchild(N7)
N4.addchild(N9)
N4.addchild(N10)

print(rootnode)