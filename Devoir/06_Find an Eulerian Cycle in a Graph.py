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


def create_adjacency_list(edges_list):
    adjacency_list = {}

    for edge in edges_list:
        # Parse each line to extract the node and its connections
        node, neighbors = edge.split(" -> ")
        node = int(node)
        neighbors = list(map(int, neighbors.split(","))) if neighbors else []

        # Assign the neighbors to the adjacency list
        adjacency_list[node] = neighbors

    return adjacency_list


# def EulerianCycle(Graph):
