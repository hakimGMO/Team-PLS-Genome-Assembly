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
    """Construct the composition graph of a collection of k-mers.

    :param Patterns: A collection Patterns of k-mers.
    :return: The composition graph CompositionGraph(Patterns), in the form of an adjacency list.
    """
    # Initialize an empty dictionary to store the adjacency list
    adj_list = {}

    # Iterate over each k-mer in Patterns
    for i, Pattern in enumerate(Patterns):
        # i is the index of the current k-mer in Patterns ; Pattern is the current k-mer
        # Add an edge labeled by Pattern to the adjacency list
        adj_list[Pattern] = []

        # Iterate over each k-mer in Patterns
        for j, Pattern_prime in enumerate(Patterns):
            # j is the index of the current k-mer in Patterns ; Pattern_prime is the current k-mer
            # Skip the current k-mer
            if i == j:
                # if the index of the current k-mer is equal to the index of the current k-mer
                continue  # skip the current k-mer

            # Add an edge labeled by Pattern_prime to the adjacency list if Suffix(Pattern) is equal to Prefix(Pattern_prime)
            if Suffix(Pattern) == Prefix(Pattern_prime):
                adj_list[Pattern].append(Pattern_prime)

    return adj_list
