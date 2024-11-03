# Construct the De Bruijn Graph of a String
"""Given a genome Text, PathGraphk(Text) is the path consisting of |Text| - k + 1 edges, where the i-th edge of this path is labeled by the i-th k-mer in Text and the i-th node of the path is labeled by the i-th (k - 1)-mer in Text. 
The de Bruijn graph DeBruijnk(Text) is formed by gluing identically labeled nodes in PathGraphk(Text).

De Bruijn Graph from a String Problem
Construct the de Bruijn graph of a string.

Given: An integer k and a string Text.

Return:DeBruijnk(Text), in the form of an adjacency list."""


# We need to create two functions: one to generate the nodes and edges of the path graph ( PathGraphk(Text)),
# and another to generate the adjacency list of the de Bruijn graph (DeBruijnk(Text)).


def PathGraphk(Text, k):
    """
    Generate the nodes and edges of the path graph from a genome Text.

    PathGraphk(Text) is the path consisting of |Text| - k + 1 edges, where the i-th edge of this path is labeled by the i-th k-mer in Text and the i-th node of the path is labeled by the i-th (k - 1)-mer in Text.

    :param Text: A string representing the genome.
    :param k: An integer representing the length of k-mers.

    :return: A tuple containing two lists:
        - nodes: A list of (k-1)-mers representing the nodes of the path graph.
        - edges: A list of k-mers representing the edges of the path graph.
    """
    # Initialize an empty list to store the nodes
    nodes = []
    # Initialize an empty list to store the edges
    edges = []

    # Iterate over the range from 0 to the length of Text - k+1
    for i in range(len(Text) - k + 1):
        # Append the i-th (k - 1)-mer in Text to the nodes list
        nodes.append(Text[i : i + k - 1])
        # Append the i-th k-mer in Text to the edges list
        edges.append(Text[i : i + k])

    return nodes, edges


def DeBruijnk(Text, k):
    """
    Generate the adjacency list of the de Bruijn graph from a genome Text.

    The de Bruijn graph DeBruijnk(Text) is formed by gluing identically labeled nodes in PathGraphk(Text).

    :param Text: A string representing the genome.
    :param k: An integer representing the length of k-mers.

    :return: A dictionary representing the adjacency list of the de Bruijn graph.
    """
    # Generate the nodes and edges of the path graph
    nodes, edges = PathGraphk(Text, k)

    # Initialize an empty dictionary to store the adjacency list
    adj_list = {}

    # Iterate over each edge in the edges list
    for edge in edges:
        # Get the prefix of the edge
        prefix = edge[: k - 1]
        # Get the suffix of the edge
        suffix = edge[1:]

        # If the prefix is not in the adjacency list, add it
        if prefix not in adj_list:
            adj_list[prefix] = []

        # If the suffix is not in the adjacency list for the prefix, add it
        if suffix not in adj_list[prefix]:
            adj_list[prefix].append(suffix)

    return adj_list
