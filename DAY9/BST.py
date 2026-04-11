class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        
    
    def insertNode(rootNode, nodeValue):
        if rootNode.data == None:
            rootNode.data = nodeValue
        elif rootNode.data > nodeValue:
            if rootNode.leftChild is None:
                rootNode.leftChild = BSTNode(nodeValue)
            else:
                BSTNode.insertNode(rootNode.leftChild, nodeValue)
        else:
            if rootNode.rightChild is None:
                rootNode.rightChild = BSTNode(nodeValue)
            else:
                BSTNode.insertNode(rootNode.rightChild, nodeValue)
        return "The value has been successfully inserted"
    
    def preOrderTraversal(rootNode):
        if not rootNode:
            return []
        result = [rootNode.data]
        result.extend(BSTNode.preOrderTraversal(rootNode.leftChild))
        result.extend(BSTNode.preOrderTraversal(rootNode.rightChild))
        return result

    def inOrderTraversal(rootNode):
        if not rootNode:
            return []
        result = []
        result.extend(BSTNode.inOrderTraversal(rootNode.leftChild))
        result.append(rootNode.data)
        result.extend(BSTNode.inOrderTraversal(rootNode.rightChild))
        return result

    def postOrderTraversal(rootNode):
        if not rootNode:
            return []
        result = []
        result.extend(BSTNode.postOrderTraversal(rootNode.leftChild))
        result.extend(BSTNode.postOrderTraversal(rootNode.rightChild))
        result.append(rootNode.data)
        return result

    def levelOrderTraversal(rootNode):
        if not rootNode:
            return []
        queue = []
        result = []
        queue.append(rootNode)
        while len(queue) > 0:
            result.append(queue[0].data)
            node = queue.pop(0)
            if node.leftChild:
                queue.append(node.leftChild)
            if node.rightChild:
                queue.append(node.rightChild)
        return result

    def printTraversal(title, values):
        print(f"{title:<12}: {' -> '.join(map(str, values))}")
    

newBST=BSTNode(None)
BSTNode.insertNode(newBST, 70)
BSTNode.insertNode(newBST, 50)
BSTNode.insertNode(newBST, 90)
BSTNode.insertNode(newBST, 30)
BSTNode.insertNode(newBST, 60)
BSTNode.insertNode(newBST, 80)
BSTNode.insertNode(newBST, 100)
BSTNode.insertNode(newBST, 20)
BSTNode.insertNode(newBST, 40)

print("                   BST Traversals                    ")
print("-" * 67)
BSTNode.printTraversal("Preorder", BSTNode.preOrderTraversal(newBST))
BSTNode.printTraversal("Inorder", BSTNode.inOrderTraversal(newBST))
BSTNode.printTraversal("Postorder", BSTNode.postOrderTraversal(newBST))
BSTNode.printTraversal("Level order", BSTNode.levelOrderTraversal(newBST))


