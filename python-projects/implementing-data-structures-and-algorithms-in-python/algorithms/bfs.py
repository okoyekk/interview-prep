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
        print()


class Graph:
    # Constructor takes a list of tuples representing edges and number of vertices in graph
    def __init__(self, edges, vertices: int):
        # A list of lists that represents an adjacency list
        self.adjList = [[] for _ in range(vertices)]
        # Add edges to the adjacency list (undirected graph)
        for (vertex_1, vertex_2) in edges:
            self.adjList[vertex_1].append(vertex_2)
            self.adjList[vertex_2].append(vertex_1)

# perform a bfs on graph
def bfs(graph, vertex, discovered):
    # create a queue for holding vertices
    queue = Queue()
    # add source vertex to discovered set and the queue
    discovered.add(vertex)
    queue.put(vertex)
    # loop till all vertices have been discovered (loop empty)
    while not queue.empty():
        # pop first vertex from queue and print it
        vertex = queue.get()
        print(vertex, end=", ")

        # add all undiscovered neighbor vertices to queue and discovered set
        adj = graph.adjList[vertex]
        for u in adj:
            if u not in discovered:
                discovered.add(u)
                queue.put(u)

def main():
    print("Tree")
    # create binary search tree
    bst = TreeNode(10)
    bst.insert(5)
    bst.insert(15)
    bst.insert(8)
    bst.insert(3)
    bst.insert(12)
    bst.insert(20)
    # print all elements using dfs
    bst.bfs()
    print("Graph")
    # list all edges in graph
    edges = [
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (9, 10), (9, 11), (0, 12)
    ]
    # total number of vertices in the graph (0–12)
    vertices = 13
    # build a graph from the given edges
    graph = Graph(edges, vertices)
    # use a set to keep track of discovered nodes
    discovered = set()
    # perform bfs on all undiscovered nodes to find all unconnected components in graph
    for i in range(vertices):
        if i not in discovered:
            bfs(graph, i, discovered)
            print()


main()
