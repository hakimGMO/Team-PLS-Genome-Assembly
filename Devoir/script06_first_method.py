# First method to solve the problem

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

# Useful functions
import pprint  # pretty print

import pyperclip

# Beƒore we need to be able to read a file with the edges of the graph and create a dictionary to store the adjacency list of the graph.
# create a dictionary to store the adjacency list of the graph.


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


# Eulerian Cycle


##
def EulerianCycle(Graph):
    """
    Finds an Eulerian cycle in a graph.
    :param Graph: An Eulerian directed graph, in the form of an adjacency list.
    :return: A list representing an Eulerian cycle in this graph.
    """
    # Initialize the cycle with any node from the graph. Here, we choose the first node in the keys of the adjacency list
    cycle = [list(Graph.keys())[0]]
    # Main loop that continues as long as there are edges in the graph to add to the cycle.
    while len(Graph) > 0:
        # When the current cycle is "closed" (the first and last nodes are the same),
        # check if this cycle contains a node with any unexplored edges.
        if cycle[0] == cycle[-1]:
            # As long as the first node of the cycle has no unexplored edges, rotate the cycle.
            # This means removing the first element of the cycle and appending it at the end.
            while cycle[0] not in Graph:
                cycle.pop(0)  # Remove the first node from the cycle.
                cycle.append(cycle[0])
                # Append this node at the end to "rotate" the cycle.
        # The last node of the current cycle becomes the new "starting point" or source to continue the traversal.
        source = cycle[-1]
        # Take one of the neighbors (or targets) of the current node in the graph (chosen randomly) and add it to the cycle.
        cycle.append(Graph[source].pop())
        # If the source node has no more neighbors (all its edges have been traversed), remove it from the graph. (clean up empty dict entries of graph)
        if len(Graph[source]) == 0:  # If the node has no more neighbors
            del Graph[source]  # delete the node from the graph
    return "->".join(cycle)  # Return the Eulerian cycle as a string


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
