# Reconstruct a String from its k-mer Composition
"""Reconstruct a string from its k-mer composition.

Given: An integer k followed by a list of k-mers Patterns.

Return: A string Text with k-mer composition equal to Patterns. (If multiple answers exist, you may return any one.)"""


"""
We can therefore summarize this solution using the following pseudocode, which relies on three problems that we have already solved:
    - The de Bruijn Graph Construction Problem;
    - The Eulerian Path Problem;
    - The String Spelled by a Genome Path Problem.
    
    StringReconstruction(Patterns)
        dB ← DeBruijn(Patterns)
        path ← EulerianPath(dB)
        Text ← PathToGenome(path)
        return Text"""

import pprint
import pyperclip


def read_kmers_from_file(filename):
    """Reads a collection of k-mers from a text file.

    :param filename: The path to the file containing k-mers.
    :return: A list of k-mers.
    """
    with open(filename, "r") as file:
        # Skip the first line which contain k (useless) and remove empty lines
        kmers = [line.strip() for line in file.readlines()[1:] if line.strip()]

    return kmers


# pprint.pp(read_kmers_from_file("Devoir/Datasets/08_dataset.txt"))

# script 5


def Prefix(Pattern):
    """Returns the prefix of a k-mer"""
    return Pattern[:-1]


def Suffix(Pattern):
    """Returns the suffix of a k-mer"""
    return Pattern[1:]


def CompositionGraph(Patterns):
    """
    Constructs the CompositionGraph of the collection of k-mers Patterns.
    :param Patterns: A collection of k-mers.
    :return: The composition graph CompositionGraph(Patterns), in the form of a tuple containing (Prefixes, Suffixes).
    """
    # Initialize an empty list to store the edges
    edges = []
    for kmer in Patterns:
        prefix = Prefix(kmer)
        suffix = Suffix(kmer)
        edges.append((prefix, suffix))
    return edges


def DeBruijn(Patterns):
    """
    Constructs the de Bruijn graph of a collection of k-mers Patterns.
    :param Patterns: A collection of k-mers.
    :return: The de Bruijn graph DeBruijn(Patterns), in the form of an adjacency list.
    """
    # Construct the CompositionGraph of Patterns
    edges = CompositionGraph(Patterns)
    # Initialize an empty dictionary to store the adjacency list
    adj_list = {}
    # Iterate over each edge in the CompositionGraph
    for edge in edges:
        # Unpack the edge into the prefix and suffix
        prefix, suffix = edge
        # Check if the prefix is already in the adjacency list
        if prefix in adj_list:
            # Append the suffix to the list of neighbors
            adj_list[prefix].append(suffix)
        else:
            # Initialize a new list with the suffix as the neighbor
            adj_list[prefix] = [suffix]
    # Sort the adjacency list by keys (prefixes) and values (suffixes) in alphabetical order
    sorted_adj_list = {k: sorted(v) for k, v in sorted(adj_list.items())}
    return sorted_adj_list


# print("The De Bruijn graph of the given k-mers is:")
# pprint.pp(DeBruijn(read_kmers_from_file("Devoir/Datasets/08_dataset.txt")))


# script 7


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

    return list(reversed(path))  # Return the Eulerian path as a list.


### script 2
def PathToGenome(kmers):
    """Reconstruct a string from its genome path.

    Input: list form : A sequence path of k-mers Pattern1, … ,Patternn such that the last k - 1 symbols of Patterni are equal to the first k-1 symbols of Patterni+1 for 1 ≤ i ≤ n-1.
    Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni (for 1 ≤ i ≤ n).
    """
    # Start with the first k-mer
    genome_string = kmers[0]

    # Append the last character of each subsequent k-mer
    for kmer in kmers[1:]:
        genome_string += kmer[-1]

    return genome_string


# Fonction finale
def StringReconstruction(filename):
    Patterns = read_kmers_from_file(filename)  # read the k-mers from the file
    dB = DeBruijn(Patterns)  # construct the de Bruijn graph
    path = EulerianPath(dB)  # find an Eulerian path in the de Bruijn graph
    Text = PathToGenome(path)  # reconstruct the string from the path
    return Text


##Results
sequence_output = StringReconstruction(
    "/Users/valentingoupille/Documents/GitHub/Team-PLS-Genome-Assembly-1/Devoir/Datasets/08_dataset_validation.txt"
)
# print("The result has been copied to the clipboard.")
pprint.pp(sequence_output)
pyperclip.copy(sequence_output)
# Verify the result with Rosalind
