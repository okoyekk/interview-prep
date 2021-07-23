from queue import Queue

class Node:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value: int):
        # insert new node based on value recursively
        if value < self.data:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        elif value > self.data:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)
        else:
            print("Duplicates not allowed!")

    def contains(self, value: int):
        # check if value is data
        if value == self.data:
            return True
        # check left subtree for value recursively
        elif value < self.data:
            if self.left == None:
                return False
            else:
                return self.left.contains(value)
        # check right subtree for value recursively
        else:
            if self.right == None:
                return False
            else:
                return self.right.contains(value)

    def printInOrder(self):
        # print left subtree
        if self.left:
            self.left.printInOrder()
        # print node value
        print(f"{self.data}, ", end='')
        # print right subtree
        if self.right:
            self.right.printInOrder()

    def bfs(self):
        # create a queue and put the parent node in it
        queue = Queue()
        queue.put(self)

        while not queue.empty():
            # print current node
            current_node = queue.get()
            print(current_node.data, end=', ')
            # put left and right child in the queue to be printed in the next level
            if current_node.left:
                queue.put(current_node.left)
            if current_node.right:
                queue.put(current_node.right)

    def find_max_depth(self):
        # iterative bfs approach to finding max depth of tree
        if self is None:
            return 0

        queue = Queue()
        queue.put(self)
        count = 0
        # iterate over tree levels
        while not queue.empty():
            size = queue.qsize()
            while size > 0:
                size -= 1
                current_node = queue.get()
                if current_node.left:
                    queue.put(current_node.left)
                if current_node.right:
                    queue.put(current_node.right)
            count += 1
        return count

    def remove_node(self, value, parent):
        # check if value is in the tree
        if not self.contains(value):
            return False

        # recurse to the subtree value is in
        if value < self.data:
            return self.left.remove_node(value, self)
        elif value > self.data:
            return self.right.remove_node(value, self)
        # when the matching node has been reached, do this
        else:
            # Case: Node has no children
            if self.left is None and self.right is None:
                if self == parent.left:
                    parent.left = None
                else:
                    parent.right = None
                self.clear_node()
            # Case: Node has 2 children
            if self.left and self.right:
                # find data of minimum right descendant of node and replace node data with it
                self.data = self.right.find_min()
                # delete that node (minimum right descendant)
                self.right.remove_node(self.data, self)
            # Case: Node has 1 child:
            else:
                # child is on the left
                if self.left and self.right is None:
                    if self == parent.left:
                        parent.left = self.left
                    else:
                        parent.right = self.left
                    self.clear_node()
                # child is on the right
                else:
                    if self == parent.left:
                        parent.left = self.right
                    else:
                        parent.right = self.right
            return True


    def clear_node(self):
        self.data = None
        self.left = None
        self.right = None

    def find_min(self):
        if self.left:
            return self.left.find_min()
        return self.data


    def __str__(self):
        self.printInOrder()
        return ""

# create binary search tree
bst = Node(10)
bst.insert(5)
bst.insert(15)
bst.insert(8)
bst.insert(3)
bst.insert(12)
bst.insert(20)
print(bst)
# remove node without children
print(bst.remove_node(20, bst))
# remove node with 1 child
print(bst.remove_node(15, bst))
# remove node with 2 children
print(bst.remove_node(5, bst))
# try to remove node that doesn't exist
print(bst.remove_node(7, bst))
print(f"Max depth: {bst.find_max_depth()}")
print(bst)
