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
    def dfs(self):
        stack = []
        current = self

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


class Graph:
    # Constructor takes a list of tuples representing edges and number of vertices in graph
    def __init__(self, edges, vertices: int):
        # A list of lists that represents an adjacency list
        self.adjList = [[] for _ in range(vertices)]
        # Add edges to the adjacency list (undirected graph)
        for (vertex_1, vertex_2) in edges:
            self.adjList[vertex_1].append(vertex_2)
            self.adjList[vertex_2].append(vertex_1)

# iterative dfs traversal of graph using a stack
def dfs(graph, vertex, discovered):
    # stack used to hold vertices
    stack = []
    # push start node to stack
    stack.append(vertex)
    # loop till stack is empty (all connected nodes have been discovered)
    while stack:
        vertex = stack.pop()
        # continue if vertex has been discovered
        if vertex in discovered:
            continue

        # print vertex and add to discovered set since it wasn't in there
        discovered.add(vertex)
        print(vertex, end=", ")
        # push each connected vertex unto stack if not yet discovered (in reverse order)
        adj = graph.adjList[vertex]
        for i in reversed(range(len(adj))):
            u = adj[i]
            if u not in discovered:
                stack.append(u)


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
    bst.dfs()

    print("Graph")
    # list all edges in graph
    edges = [
        (1, 2), (1, 7), (1, 8), (2, 3), (2, 6), (3, 4),
        (3, 5), (8, 9), (9, 10), (9, 11)
    ]
    # total number of vertices in the graph (0–12)
    vertices = 13
    # build a graph from the given edges
    graph = Graph(edges, vertices)
    # use a set to keep track of discovered nodes
    discovered = set()
    # Perform iterative DFS traversal from all undiscovered nodes to
    # cover all unconnected components of a graph
    for i in range(vertices):
        if i not in discovered:
            dfs(graph, i, discovered)

main()
