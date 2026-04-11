class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insertnode(self.root, value)

    def insertnode(self, rootnode, value):
        if value < rootnode.data:
            if rootnode.left is None:
                rootnode.left = Node(value)
            else:
                self.insertnode(rootnode.left, value)
        else:
            if rootnode.right is None:
                rootnode.right = Node(value)
            else:
                self.insertnode(rootnode.right, value)

    # Height of tree
    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))

    # Print tree with structure + branches
    def print_tree(self):
        h = self.height(self.root)
        queue = [self.root]

        for level in range(h):
            space = " " * (2 ** (h - level - 1))
            next_queue = []

            # Print nodes
            print(space, end="")
            for node in queue:
                if node:
                    print(node.data, end=space)
                    next_queue.append(node.left)
                    next_queue.append(node.right)
                else:
                    print(" ", end=space)
                    next_queue.append(None)
                    next_queue.append(None)
            print()

            # Print branches (/ \)
            if level < h - 1:
                print(space, end="")
                for node in queue:
                    if node:
                        print("/", end=" ")
                        print("\\", end=space[:-1] if len(space) > 1 else "")
                    else:
                        print("  ", end=space)
                print("\n")

            queue = next_queue


# object creation
btobj = BinaryTree()
btobj.insert(50)
btobj.insert(30)
btobj.insert(70)
btobj.insert(20)
btobj.insert(40)
btobj.insert(60)
btobj.insert(80)

print("\nTree Structure with branches:\n")
btobj.print_tree()