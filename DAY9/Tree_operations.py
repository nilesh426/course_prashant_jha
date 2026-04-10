#creating a object means creating a separate node
class Node:
    #create a node in the tree
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        #insert root node in if there is no root node
        if self.root == None:
            self.root = Node(value)
        else:   
            self.insertnode(self.root,value)

    def insertnode(self,rootnode,value):
        if value < rootnode.value:
            if rootnode.left is None:
                rootnode.left=Node(value)
            else:
                self.insertnode(rootnode.left,value)
        else:
            if rootnode.right is None:
                rootnode.right=Node(value)
            else:
                self.insertnode(rootnode.left,value)



btobj= BinaryTree()
btobj.insert(50)
btobj.insert(30)
btobj.insert(70)

