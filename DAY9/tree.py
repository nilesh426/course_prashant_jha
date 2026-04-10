#Full binary tree: Each node has either 0 or 2 children . No node has a single child.

#Complete binary tree: .All levels except possibly the last are completely filled and
#                      .Nodes in the last level are filled from left to right

#Perfect binary tree: .All internal nodes have exactly 2 nodes.
#                     .All leaf nodes are at the same level.


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

#object creation
rootNode=Tree("Drinks")
hot = Tree("Hot")
cold = Tree("Cold")
tea = Tree("Tea")
coffee = Tree("Coffee")
nonAlcoholic = Tree("Non-Alcoholic")
Alcoholic = Tree("Alcoholic")

#add child nodes in tree
rootNode.addChild(hot)
rootNode.addChild(cold)

hot.addChild(tea)
hot.addChild(coffee)

cold.addChild(nonAlcoholic)
cold.addChild(Alcoholic)

print(rootNode)