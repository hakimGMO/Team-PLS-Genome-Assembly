# Find an Eulerian Path in a Graph
"""In “Find an Eulerian Cycle in a Graph”, we defined an Eulerian cycle. 
A path that traverses each edge of a graph exactly once (but does not necessarily return to its starting node is called an Eulerian path.

Eulerian Path Problem
Find an Eulerian path in a graph.

Given: A directed graph that contains an Eulerian path, where the graph is given in the form of an adjacency list.

Return: An Eulerian path in this graph."""

# Useful functions
import pprint  # pretty print
import random  # random choice
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
# print(read_edges_from_file("Devoir/Datasets/07_dataset.txt"))


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
# pprint.pp(create_adjacency_list(("Devoir/Datasets/07_dataset.txt")))


def EulerianPath(Graph):
    """Find an Eulerian path in a graph."""

    def find_start_node(Graph):
        """Find the starting node for the Eulerian path."""
        # Initialize dictionaries for counting in-degrees and out-degrees of each node.
        in_degrees = {
            node: 0 for node in Graph
        }  # Initialize in-degrees to 0 for all nodes.
        out_degrees = {
            node: len(neighbors) for node, neighbors in Graph.items()
        }  # Initialize out-degrees for each node.

        # Calculate in-degrees for each node by iterating through each neighbor in the adjacency list.
        for (
            neighbors
        ) in Graph.values():  # Iterate through the adjacency list of each node.
            for neighbor in neighbors:  # Iterate through the neighbors of the node.
                if (
                    neighbor not in in_degrees
                ):  # If the neighbor is not in the in-degrees dictionary, add it.
                    in_degrees[neighbor] = 0  # Initialize the in-degree to 0.
                in_degrees[neighbor] += 1  # Increment the in-degree of the neighbor.

        # Initialize start_node as None (default value if no start node is found).
        start_node = None

        # Determine the start node by checking degree imbalances (out-degree - in-degree).
        for node in Graph:  # Iterate through each node in the graph.
            # If a node has one more outgoing edge than incoming, it's the start of the path.
            if (
                out_degrees[node] - in_degrees[node] == 1
            ):  # If the degree imbalance is 1.
                start_node = node  # Set the start node to the current node.
                break  # Exit the loop.
            # Otherwise, choose any node with an outgoing edge as the start node.
            elif out_degrees[node] > 0:  # If the node has outgoing edges.
                start_node = node  # Set the start node to the current node.

        return start_node  # Return the start node for the Eulerian path.

    # Initialize the stack with the starting node found by find_start_node.
    stack = [find_start_node(Graph)]

    # Initialize an empty list to hold the Eulerian path.
    path = []

    # While there are still nodes in the stack to process:
    while stack:
        # Look at the last node in the stack (current node).
        node = stack[-1]

        # If the current node has any outgoing edges:
        if node in Graph and Graph[node]:
            # Remove the edge from the adjacency list and add it to the stack.
            stack.append(Graph[node].pop())

        else:
            path.append(
                stack.pop()
            )  # Remove the last node from the stack and add it to the path.

    return "->".join(map(str, reversed(path)))  # Return the Eulerian path as a string.


# Example of usage with the short Rosalind example
test_adj_list = {0: [2], 1: [3], 2: [1], 3: [0, 4], 6: [3, 7], 7: [8], 8: [9], 9: [6]}

# Example of usage with the short Rosalind example
pprint.pp(EulerianPath(test_adj_list))


def EulerianPathfromfile(filename):
    """Find an Eulerian Path in a graph.
    :param filename: The path to the file containing the adjacency list of the graph.
    :return: Eulerian Path of this graph.
    """
    # Create the adjacency list of the graph
    graph = create_adjacency_list(filename)
    # Find the Eulerian cycle
    Path = EulerianPath(graph)
    return Path


# Test with the Rosalind dataset
pyperclip.copy(
    EulerianPathfromfile("Devoir/Datasets/07_dataset.txt")
)  # Copy the result to the clipboard
pprint.pp(EulerianPathfromfile("Devoir/Datasets/07_dataset.txt"))
