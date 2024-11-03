# Construct the De Bruijn Graph of a Collection of k-mers

"""Given an arbitrary collection of k-mers Patterns (where some k-mers may appear multiple times),
we define CompositionGraph(Patterns) as a graph with |Patterns| isolated edges. 
Every edge is labeled by a k-mer from Patterns, and the starting and ending nodes of an edge are labeled by the prefix and suffix of the k-mer labeling that edge. 
We then define the de Bruijn graph of Patterns, denoted DeBruijn(Patterns), by gluing identically labeled nodes in CompositionGraph(Patterns), which yields the following algorithm."""


import pyperclip  # to copy the result to the clipboard


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
        prefix, suffix = (
            edge  # prefix is the first element of the edge, suffix is the second element of the edge
        )
        # Check if the prefix is already in the adjacency list
        if prefix in adj_list:
            # Append the suffix to the list of neighbors
            adj_list[prefix].append(suffix)
        else:
            # Initialize a new list with the suffix as the neighbor
            adj_list[prefix] = [suffix]
    return adj_list
