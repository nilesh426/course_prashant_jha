# import QueueLinkedList as queue

class BSTNode:
    def __init__(self):
        self.data=self.data
        self.leftChild=None
        self.rightChild=None

    def insertNode(rootNode, nodeValue):
        if rootNode.data == None:
            rootNode.data = nodeValue
        elif rootNode.data > nodeValue:
            if rootNode.leftChild is None:
                rootNode.leftChild = BSTNode(nodeValue)
            else:
                BSTNode.inserNode(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild is None:
                rootNode.rightChild = BSTNode(nodeValue)
            else:
                BSTNode.inserNode(rootNode.rightChild, nodeValue)