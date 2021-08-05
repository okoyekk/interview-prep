import numpy as np
from queue import Queue
from typing import List
import sys

class UndirectedGraph:
    def __init__(self, edges, vertices):
        # A list of lists that represents an adjacency list for each node
        self.adjList = [[] for _ in range(vertices)]
        # Add edges to the adjacency list (undirected graph)
        for (vertex_1, vertex_2) in edges:
            self.adjList[vertex_1].append(vertex_2)
            self.adjList[vertex_2].append(vertex_1)


class DirectedGraph:
    def __init__(self, edges, vertices):
        # A list of lists that represents an adjacency list for each node
        self.adjList = [[] for _ in range(vertices)]
        # Add edges to the adjacency list (Directed graph)
        for (vertex_1, vertex_2) in edges:
            self.adjList[vertex_1].append(vertex_2)


class TreeNode:
    def __init__(self, data: int=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.data:
            if self.left:
                self.left.insert(value)
            else:
                self.left = TreeNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = TreeNode(value)

    def printInOrder(self):
        # print left subtree
        if self.left:
            self.left.printInOrder()
        # print node value
        print(f"{self.data}, ", end='')
        # print right subtree
        if self.right:
            self.right.printInOrder()


class LLNode():
    # LLNode Class
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList():
    # Linked list class with standard and extra methods
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def get_size(self):
        return self.size

    def add_node(self, data):
        # New node's next pointer is set to the current head
        new_node = LLNode(data, self.head)
        # current head is set to the new node
        self.head = new_node
        # Linked list size is incremented by 1
        self.size += 1


"""
# Route between nodes
def route_between(graph, start, end):
    # method checks if there is a path between start and end nodes
    # check if start == end
    if start == end:
        return True
    # do a bfs search from start and if end gets discovered, node exists (return True)
    discovered = set()
    queue = Queue()
    # add start node to queue
    queue.put(start)
    # traverse graph usng queue
    while not queue.empty():
        vertice = queue.get()
        neighbors = graph.adjList[vertice]
        for u in neighbors:
            if u not in discovered:
                # check if current neighbor is end
                if u == end:
                    return True
                discovered.add(u)
                queue.put(u)
    # if end was not found, return False
    return False


# directed edges in graph
edges = [
    (0, 3), (0, 1), (1, 3), (2, 5), (3, 4), (3, 5),
    (4, 2), (4, 5), (4, 8), (5, 8), (6, 7), (8, 6),
    (9, 7)
]
# number of vertices in graph
vertices = 10
graph = DirectedGraph(edges, vertices)
print(route_between(graph, 0, 7))
print(route_between(graph, 0, 9))
print(route_between(graph, 0, 0))
"""


"""
# Minimal tree
def minimal_tree(elements: List[int]):
    # get middle element and make it root
    middle_index = (len(elements) - 1) // 2
    root = TreeNode(elements[middle_index])
    # create minimum tree for both halves of array
    # and add them to root
    root.left = create_minimal_tree(root, 0, middle_index - 1, elements)
    root.right = create_minimal_tree(root, middle_index + 1, len(elements) - 1, elements)
    return root

def create_minimal_tree(node, start, end, elements):
    # handle base case
    if start > end:
        return None
    # create a new node at midpoint of subarray and create minimal trees
    # for left and right children, then return it
    midpoint = (start + end) // 2
    new_node = TreeNode(elements[midpoint])
    new_node.left = create_minimal_tree(new_node, start, midpoint - 1, elements)
    new_node.right = create_minimal_tree(new_node, midpoint + 1, end, elements)
    return new_node

# test minimal_tree method by printing node in order
elements = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
new_tree = minimal_tree(elements)
new_tree.printInOrder()
"""

"""
# list of depths
def list_of_depths(root):
    # perform a bfs traversal of each level the tree using a queue and
    # creates a new linked list for each level
    queue = Queue()
    queue.put(root)
    # create a list to hold all linked list and add root to the first linked list
    lists = []
    lists.append(LinkedList())
    lists[-1].add_node(root)
    while not queue.empty():
        size = queue.qsize()
        # create a linked list for each level
        lists.append(LinkedList())
        level_list = lists[-1]
        while size > 0:
            current_node = queue.get()
            # add child nodes of nodes in each level to the linked list
            if current_node.left:
                queue.put(current_node.left)
                level_list.add_node(current_node.left)
            if current_node.right:
                queue.put(current_node.right)
                level_list.add_node(current_node.right)
            size -= 1
    return lists

# Create a tree with 3 levels
my_tree = TreeNode(6)
for i in (3, 9, 1, 4, 7, 10, 2, 5, 8, 11):
    my_tree.insert(i)
# get list of depths
tree_lists = list_of_depths(my_tree)
# print nodes at each depth
index = 0
for tree_list in tree_lists:
    current = tree_list.head
    while current:
        print(current.data.data, end=", ")
        current = current.next
    print()
"""

"""
# Check Balanced
def check_balance(root):
    if check_height(root) == -sys.maxsize:
        return False
    return True


def check_height(root):
    # base case, return -1 if root is none
    if not root:
        return -1
    # get heights of child nodes
    left_height = check_height(root.left)
    right_height = check_height(root.right)
    # check if either subtree is already unbalanced
    if (left_height == -sys.maxsize) or (right_height == -sys.maxsize):
        return -sys.maxsize
    # check if current tree is unbalanced
    difference = abs(left_height - right_height)
    if difference > 1:
        return -sys.maxsize
    else:
        # return height of higher subtree subtree + 1
        return max(right_height, left_height) + 1


# Create a tree with 3 levels
my_tree = TreeNode(6)
for i in (3, 9, 1, 4, 7, 10, 2, 5, 8, 11):
    my_tree.insert(i)
print(check_balance(my_tree))
"""

"""
# Validate BST
def is_bst(root):
    # check if subtree is a bst recursively
    return check_bst(root, -sys.maxsize, sys.maxsize)


def check_bst(node, minimum, maximum):
    # base case: check if node exists
    if not node:
        return True
    # check if node is between acceptable range
    if (node.data < minimum) or (node.data > maximum):
        return False
    # adjust minimum and maximum values and recurse on both children
    if not (check_bst(node.left, minimum, node.data) or check_bst(node.right, node.data, maximum)):
        return False
    return True



# Create a tree with 3 levels
my_tree = TreeNode(6)
for i in (3, 9, 1, 4, 7, 10, 2, 5, 8, 11):
    my_tree.insert(i)
print(is_bst(my_tree))
bad_tree = TreeNode(6)
bad_tree.left = TreeNode(9)
bad_tree.right = TreeNode(0)
print(is_bst(bad_tree))
"""


# Successor -> Passing on this cos i need to modify the node class
# Understoof the concept


# Build order -> Solved already - topological sort
# Understood


"""
# First common ancestor
def get_ancestor(tree: TreeNode, node_1: int, node_2: int):
    # check if both nodes are in tree
    if not (covers(tree, node_1) and covers(tree, node_2)):
        return "Either node is not in tree"
    return get_ancestor_util(tree, node_1, node_2)


def get_ancestor_util(tree: TreeNode, node_1: int, node_2: int):
    # Handle base case (empty root)
    if root == None:
        return None
    # return root if either node is the parent of the other
    if (root.data == node_1) or (root.data == node_2):
        return root.data
    # check if both nodes are in either subtree and call get_ancestor_util recursively
    is_left_tree = covers(root.left, node_1) and covers(root.left, node_2)
    is_right_tree = covers(root.right, node_1) and covers(root.right, node_2)
    # left subtree
    if is_left_tree and (not is_right_tree):
        return get_ancestor_util(root.left, node_1, node_2)
    # right subtree
    if is_right_tree and (not is_left_tree):
        return get_ancestor_util(root.right, node_1, node_2)
    # if both nodes are in different subtrees, lowest
    # common ancestor has been found, so return it
    return root.data


def covers(root: TreeNode, node: int):
    # check if a node is in a root's subtree
    if root == None:
        return False
    if root.data == node:
        return True
    return covers(root.left, node) or covers(root.right, node)


def main():
    # build a tree
    my_tree = TreeNode(10)
    nodes = [6, 17, 3, 8, 14, 20, 1, 5, 7, 9, 12, 15, 19, 25]
    for i in nodes:
        my_tree.insert(i)
    print(get_ancestor(my_tree, 12, 25))



main()
"""


# BST Sequences -> this is a leetcode hard question so I'm passing on this
# (Beyone my scope)

"""
# check subtree
def check_subtree(t1: TreeNode, t2: TreeNode) -> bool:
    # do a pre order traversal of both nodes and
    # check if t2 is a sublist of t1
    t1_list = []
    t2_list = []
    preorder_dfs(t1, t1_list)
    preorder_dfs(t2, t2_list)
    # check if t2 is longer than t1
    if len(t2_list) > len(t1_list):
        return False

    # iterate over t1_list checking if t2 is a sublist
    for i in range(len(t1_list) - len(t2_list) + 1):
        if t1_list[i: i+len(t2_list)] == t2_list:
            return True
    return False


def preorder_dfs(root: TreeNode, arr: List[int]):
    arr.append(root.data)
    # add placeholders for leaf nodes
    if root.left:
        preorder_dfs(root.left, arr)
    else:
        arr.append("|")
    if root.right:
        preorder_dfs(root.right, arr)
    else:
        arr.append("|")



def main():
    # create tree
    my_tree = TreeNode(15)
    nodes = [10, 20, 5, 13, 17, 23]
    for i in nodes:
        my_tree.insert(i)
    subtree = my_tree.right
    print(check_subtree(my_tree, subtree))
    bad_subtree = TreeNode(10)
    print(check_subtree(my_tree, bad_subtree))


main()
"""

# LAST 2 QUESTIONS ARE TODOs
