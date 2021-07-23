class Node:
    def __init__(self, data:int = None):
        self.data = data
        self.left = None
        self.right = None

def is_bst(root):
    INT_MAX = 100000000
    INT_MIN = -100000000
    return validate(root, INT_MIN, INT_MAX)

def validate(root, minimum, maximum):
    # base case
    if root is None:
        return True

    # return False if data is greater or less than minimum or maximum
    if root.data < minimum or root.data > maximum:
        return False

    # check subtrees recursively while tightening the min/max window
    # this makes sure a node value is not greater/less than its root when its on
    # the left/right subtree respectively
    return validate(root.left, minimum, root.data - 1) and validate(root.right, root.data + 1, maximum)


def main():
    valid_tree = Node(7)
    valid_tree.left = Node(4)
    valid_tree.right = Node(9)
    valid_tree.left.left = Node(1)
    valid_tree.left.right = Node(6)
    print(is_bst(valid_tree))

main()
