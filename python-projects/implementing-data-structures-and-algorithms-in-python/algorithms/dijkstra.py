from typing import List, Dict

def dijkstra(nodes: List[int], edges: Dict, source_index=0):
    # set distance to every node to infinity and source distance to 0
    path_lengths = {v: float('inf') for v in nodes}
    path_lengths[source_index] = 0

    adjacent_nodes = {v: {} for v in nodes}
    # represent directed edges in a dictionary
    for (u, v), weight in edges.items():
        adjacent_nodes[u][v] = weight
    # print(adjacent_nodes)
    # initialize a tempoaray nodes list with all nodes
    temporary_nodes = [v for v in nodes]
    while len(temporary_nodes) > 0:
        # get nearest node to source and remove it from temporary node list
        upper_bounds = {v: path_lengths[v] for v in temporary_nodes}
        u = min(upper_bounds, key=upper_bounds.get)
        temporary_nodes.remove(u)
        # iterate through all nodes adjacent to that node
        for v, weight in adjacent_nodes[u].items():
            # update distance to each connected node with new distance if new distance is smaller
            path_lengths[v] = min(path_lengths[v], path_lengths[u] + weight)
    return path_lengths


def main():
    # create nodes, edges and pass them into the dijkstra function
    nodes = [1, 2, 3, 4, 5, 6]
    edges = {
        (1, 2): 2, (1, 3): 4,
        (2, 3): 1, (2, 4): 7,
        (3, 5): 3,
        (4, 6): 1,
        (5, 4): 2, (5, 6): 5
    }
    print(dijkstra(nodes, edges, 1))


if __name__ == '__main__':
    main()
