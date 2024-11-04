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

# Useful functions
import pprint  # pretty print
import random  # random choice
from copy import deepcopy  # deep copy of the graph
import pyperclip


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
    """
    Finds an Eulerian cycle in a graph.
    :param Graph: An Eulerian directed graph, in the form of an adjacency list.
    :return: A list representing an Eulerian cycle in this graph.
    """
    # Copy of the remaining edges in a dictionary using deepcopy
    remaining_edges = deepcopy(Graph)

    # Check if there are remaining edges to visit
    def has_remaining_edges():
        return any(remaining_edges[node] for node in remaining_edges)

    # Perform a random walk starting from a given node
    def random_walk(start):
        path = [start]
        current_node = start
        while remaining_edges[current_node]:
            next_node = random.choice(remaining_edges[current_node])
            remaining_edges[current_node].remove(next_node)
            current_node = next_node
            path.append(current_node)
        return path

    # Choose a starting node that has neighbors
    possible_start_nodes = [node for node in Graph if Graph[node]]
    start_node = random.choice(possible_start_nodes)

    # Initial cycle
    cycle = random_walk(start_node)
    while has_remaining_edges():
        for pos, node in enumerate(cycle):
            if remaining_edges[node]:  # If we find a node with remaining edges
                # Start a new cycle from this node and perform a random walk
                new_cycle = cycle[pos:] + cycle[1 : pos + 1]
                cycle_extension = random_walk(node)[1:]
                cycle = new_cycle + cycle_extension
                break

    return "->".join(cycle)


# Example of usage with the shor~t Rosalind example
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
pprint.pp(EulerianCycle(test_adj_list))


def EulerianCyclefromfile(filename):
    """Find an Eulerian cycle in a graph.
    :param filename: The path to the file containing the adjacency list of the graph.
    :return: An Eulerian cycle in this graph.
    """
    # Create the adjacency list of the graph
    graph = create_adjacency_list(filename)
    # Find the Eulerian cycle
    cycle = EulerianCycle(graph)
    return cycle


# Test with the Rosalind dataset
pyperclip.copy(
    EulerianCyclefromfile("Devoir/Datasets/06_dataset.txt")
)  # Copy the result to the clipboard
