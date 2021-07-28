class TreeNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value: int):
        # insert new node based on value recursively
        if value < self.data:
            if self.left == None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        elif value > self.data:
            if self.right == None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
        else:
            print("Duplicates not allowed!")

# depth first search using a stack
def dfs(start: TreeNode):
    stack = []
    current = start

    while True:
        # go to leftmost child of node
        if current:
            # add parent nodes to stack before going deeper
            stack.append(current)
            current = current.left
        # if current node doesn't exist (dead end), backtrack using stack
        elif stack:
            current = stack.pop()
            print(current.data, end=", ")
            # go down right subtree
            current = current.right
        # else, all nodes have been printed so return
        else:
            break
    print()

# create binary search tree
bst = TreeNode(10)
bst.insert(5)
bst.insert(15)
bst.insert(8)
bst.insert(3)
bst.insert(12)
bst.insert(20)
# print all elements using dfs
dfs(bst)
