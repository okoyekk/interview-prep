class DirectedGraph:
    def __init__(self, edges, vertices):
        # A list of lists that represents an adjacency list for each node
        self.adjList = [[] for _ in range(vertices)]
        # Add edges to the adjacency list (Directed graph)
        for (vertex_1, vertex_2) in edges:
            self.adjList[vertex_1].append(vertex_2)


def topological_sort(graph: DirectedGraph):
    # Topological sort based on dfs
    # First check if graph has a cycle
    if has_cycle(graph):
        return []
    # use a stack to store ordering of nodes and set to keep track of seen nodes
    stack = []
    visited = set()
    # add nodes without dependencies to sorted vertices
    for i in range(len(graph.adjList)):
        if i not in visited:
            visit(graph, i, stack, visited)
    sorted_nodes = list(reversed(stack))
    return sorted_nodes


def visit(graph: DirectedGraph, node: int, stack: list, visited: set):
    # get nodes which depend on it
    adjacents = graph.adjList[node]
    # add node to visited set
    visited.add(node)
    for u in adjacents:
        # visit all adjacent nodes that haven't been visited
        if u not in visited:
            visit(graph, u, stack, visited)
    # add node to stack when all adjacent nodes have been visited
    stack.append(node)


def has_cycle(graph: DirectedGraph):
    # create a set for tracking visited nodes
    visited = set()
    # iterate over all nodes in graph and check if any node is in a cycle
    for i in range(len(graph.adjList)):
        visited.add(i)
        # traverse adjacent nodes
        for j in graph.adjList[i]:
            if has_cycle_util(graph, visited, j):
                return True
        # remove node from visited set (not in cycle)
        visited.remove(i)
    return False


def has_cycle_util(graph, visited, node):
    # cycle exists if node is already visited
    if node in visited:
        return True

    visited.add(node)
    # traverse adjacent nodes checkng for cycles recursively
    for i in graph.adjList[node]:
        if has_cycle_util(graph, visited, i):
            return True
    # remove node from visited set (not in cycle)
    visited.remove(node)
    return False


def main():
    vertices = 4
    # edges = [
    #     (0, 3), (5, 1), (1, 3),
    #     (5, 0), (3, 2)
    # ]
    # edges = [
    #     (5, 2), (0, 2), (5, 0),
    #     (4, 2), (4, 1), (3, 1),
    #     (0, 3)
    # ]
    edges = [
        (0, 2), (2, 3),
        (3, 1), (1, 0)
    ]
    my_graph = DirectedGraph(edges, vertices)
    print(topological_sort(my_graph))


main()
