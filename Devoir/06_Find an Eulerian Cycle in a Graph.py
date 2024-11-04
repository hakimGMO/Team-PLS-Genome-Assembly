# Find an Eulerian Cycle in a Graph
"""A cycle that traverses each edge of a graph exactly once is called an Eulerian cycle, 
and we say that a graph containing such a cycle is Eulerian.
The following algorithm constructs an Eulerian cycle in an arbitrary directed graph.

    EULERIANCYCLE(Graph)
        form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
        while there are unexplored edges in Graph
            select a node newStart in Cycle with still unexplored edges
            form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking
            Cycle ← Cycle’
        return Cycle"""

"""Eulerian Cycle Problem
Find an Eulerian cycle in a graph.

Given: An Eulerian directed graph, in the form of an adjacency list.

Return: An Eulerian cycle in this graph."""

# Beƒore we need to be able to read a file with the edges of the graph and create a dictionary to store the adjacency list of the graph.
# create a dictionary to store the adjacency list of the graph.


import pprint


def read_edges_from_file(filename):
    """Reads a collection of edges from a text file.
        :param filename: The path to the file containing edges.
        :return: A list of edges.
        Example:

    Input:
    0 -> 3 # each line is an edge
    1 -> 0
    2 -> 1,6
    3 -> 2
    4 -> 2
    5 -> 4
    6 -> 5,8
    7 -> 9
    8 -> 7
    9 -> 6

    Output: ['0 -> 3', '1 -> 0', '2 -> 1,6', '3 -> 2', '4 -> 2', '5 -> 4', '6 -> 5,8', '7 -> 9', '8 -> 7', '9 -> 6']

    """
    with open(filename, "r") as file:
        # remove empty lines and add to list
        edges_list = [line.strip() for line in file if line.strip()]

    return edges_list


# Example of usage
# print(read_edges_from_file("Devoir/Datasets/06_dataset.txt"))


# create a dictionary to store the adjacency list of the graph.
def create_adjacency_list(filename):
    """Creates an adjacency list from a list of edges.
    :param filename: The path to the file containing edges.
    :return: A dictionary representing the adjacency list of the graph.
    """
    # read the edges from the file and convert to a list
    edges_list = read_edges_from_file(filename)
    adjacency_list = {}

    for edge in edges_list:
        # Parse each line to extract the node and its connections
        node, neighbors = edge.split(" -> ")  # split the edge into node and neighbors
        # convert the neighbors to a list
        neighbors = neighbors.split(",") if neighbors else []

        # Assign the neighbors to the adjacency list
        adjacency_list[node] = neighbors

    return adjacency_list


# Example of usage :
# pprint.pp(create_adjacency_list(("Devoir/Datasets/06_dataset.txt")))


def EulerianCycle(Graph):
    """Find an Eulerian cycle in a graph.
    :param Graph: An Eulerian directed graph, in the form of an adjacency list.
    :return: An Eulerian cycle in this graph.

    form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
        while there are unexplored edges in Graph
            select a node newStart in Cycle with still unexplored edges
            form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking
            Cycle ← Cycle’
        return Cycle
    """
    # Initialize an empty list to store the Eulerian cycle
    Cycle = []
    # Select a random node to start the cycle
    start_node = next(iter(Graph))
    Cycle.append(start_node)
    # Initialize a list to store the current cycle
    current_cycle = [start_node]

    while current_cycle:
        current_node = current_cycle[-1]
        # Check if the current node has unexplored edges
        if current_node in Graph and Graph[current_node]:
            # Choose a random neighbor of the current node
            neighbor = Graph[current_node].pop()
            current_cycle.append(neighbor)
            Cycle.append(neighbor)
        else:
            # Backtrack to find the unexplored edges
            for i in range(len(Cycle)):
                if Cycle[i] in Graph and Graph[Cycle[i]]:
                    current_cycle = current_cycle[: i + 1]
                    break

    return Cycle


# Example of usage with the short Rosalind example
test_adj_list = {
    "0": ["3"],
    "1": ["0"],
    "2": ["1", "6"],
    "3": ["2"],
    "4": ["2"],
    "5": ["4"],
    "6": ["5", "8"],
    "7": ["9"],
    "8": ["7"],
    "9": ["6"],
}

# Example of usage with the short Rosalind example
print(EulerianCycle(test_adj_list))
