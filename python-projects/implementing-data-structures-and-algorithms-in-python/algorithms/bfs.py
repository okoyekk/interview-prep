from queue import Queue

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

# Breadth First search for a tree
def bfs(start):
    # create a queue and put the parent node in it
    queue = Queue()
    queue.put(start)

    while not queue.empty():
        # print current node
        current_node = queue.get()
        print(current_node.data, end=', ')
        # put left and right child in the queue to be printed in the next level
        if current_node.left:
            queue.put(current_node.left)
        if current_node.right:
            queue.put(current_node.right)

# create binary search tree
bst = TreeNode(10)
bst.insert(5)
bst.insert(15)
bst.insert(8)
bst.insert(3)
bst.insert(12)
bst.insert(20)
# print all elements using dfs
bfs(bst)
