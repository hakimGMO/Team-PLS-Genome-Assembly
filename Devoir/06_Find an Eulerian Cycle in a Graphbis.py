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


# Find an Eulerian Cycle in a given graph
#
# Graph has to be strongly connected and balanced.
#
# @param graph:  A dict of lists, sources are dict keys, targets are in the lists
##
def EulerianCycle(Graph):
    # init cycle with any node
    cycle = [list(Graph.keys())[0]]
    # run until all edges are moved from graph to cycle
    while len(Graph) > 0:
        # whenever cycle closes rotate to a node with remaining targets
        if cycle[0] == cycle[-1]:
            while cycle[0] not in Graph:
                cycle.pop(0)
                cycle.append(cycle[0])
        # the last node of cycle is the new source
        source = cycle[-1]
        # move one target at a time from graph to the end of cycle
        cycle.append(Graph[source].pop())
        # clean up empty dict entries of graph
        if len(Graph[source]) == 0:
            del Graph[source]
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
adj_list = create_adjacency_list("Devoir/Datasets/06_datasetbis.txt")
cycle = EulerianCycle(adj_list)
pyperclip.copy(cycle)  # Copy the result to the clipboard
