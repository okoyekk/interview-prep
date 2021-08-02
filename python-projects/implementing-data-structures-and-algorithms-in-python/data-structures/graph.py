class Graph:
    # Constructor takes a list of tuples representing edges and number of vertices in graph
    def __init__(self, edges, vertices: int):
        # A list of lists that represents an adjacency list for each node
        self.adjList = [[] for _ in range(vertices)]
        # Add edges to the adjacency list (undirected graph)
        for (vertex_1, vertex_2) in edges:
            self.adjList[vertex_1].append(vertex_2)
            self.adjList[vertex_2].append(vertex_1)


# recursively print all vertices in the graph using dfs
def traverse(graph: Graph, vertex: int, discovered: set):
    # add node to the discovered set and print it
    discovered.add(vertex)
    print(vertex, end=", ")

    # traverse through all undiscovered vertices connected to
    # current vertex recursively
    for i in graph.adjList[vertex]:
        if i not in discovered:
            traverse(graph, i, discovered)

def main():
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
    # Perform DFS traversal from all undiscovered nodes to
    # cover all unconnected components of a graph
    for i in range(vertices):
        if i not in discovered:
            traverse(graph, i, discovered)

main()
