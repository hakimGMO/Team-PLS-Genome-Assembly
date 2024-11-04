# Construct the Overlap Graph of a Collection of k-mers

"""In this chapter, we use the terms prefix and suffix to refer to the first k − 1 nucleotides and last k − 1 nucleotides of a k-mer, respectively.

Given an arbitrary collection of k-mers Patterns, we form a graph having a node for each k-mer in Patterns and connect k-mers Pattern and Pattern' by a directed edge if Suffix(Pattern) is equal to Prefix(Pattern'). 
The resulting graph is called the overlap graph on these k-mers, denoted Overlap(Patterns).

Overlap Graph Problem
Construct the overlap graph of a collection of k-mers.

Given: A collection Patterns of k-mers.

Return: The overlap graph Overlap(Patterns), in the form of an adjacency list."""


import pyperclip  # to copy the result to the clipboard


def Prefix(Pattern):
    """Returns the prefix of a k-mer"""
    return Pattern[:-1]


def Suffix(Pattern):
    """Returns the suffix of a k-mer"""
    return Pattern[1:]


def read_kmers_from_file(filename):
    """Reads a collection of k-mers from a text file.

    :param filename: The path to the file containing k-mers.
    :return: A list of k-mers.
    """
    with open(filename, "r") as file:
        # remove empty lines and add to list
        kmers = [line.strip() for line in file if line.strip()]

    return kmers


def Overlap(Patterns):
    """Construct the overlap graph of a collection of k-mers.

    :param Patterns: A collection Patterns of k-mers.
    :return: The overlap graph Overlap(Patterns), in the form of an adjacency list.
    """
    # Initialize an empty dictionary to store the adjacency list
    adj_list = {}

    # Iterate over each k-mer in Patterns
    for i, Pattern in enumerate(Patterns):
        # i is the index of the current k-mer in Patterns ; Pattern is the current k-mer
        # Iterate over each k-mer in Patterns
        for j, Pattern_prime in enumerate(Patterns):
            # j is the index of the current k-mer in Patterns ; Pattern_prime is the current k-mer
            # Skip the current k-mer
            if i == j:
                # if the index of the current k-mer is equal to the index of the current k-mer
                continue  # skip the current k-mer

            # Check if Suffix(Pattern) is equal to Prefix(Pattern_prime)
            if Suffix(Pattern) == Prefix(Pattern_prime):
                if Pattern not in adj_list:  # if Pattern is not in the adjacency list
                    adj_list[Pattern] = []  # add Pattern to the adjacency list
                adj_list[Pattern].append(Pattern_prime)
                # add Pattern_prime to the adjacency list of Pattern
    # print(adj_list) # example: {'ATGCG': ['TGCGC', 'GCATG'], 'GCATG': ['CATGC'], 'CATGC': ['ATGCG'], 'AGGCA': ['GGCAT'], 'GGCAT': ['GCATG']}
    return adj_list  # return the adjacency list


def adj_list_to_string(overlap_adj_list):
    """Convert the overlap graph to a string representation.

    :param adj_list: The overlap graph in the form of an adjacency list.
    :return: A string representation of the overlap graph.
    """
    return "\n".join(f"{k} -> {', '.join(v)}" for k, v in overlap_adj_list.items())


# Example usage
filename = "Devoir/Datasets/03_dataset.txt"  #  file path
kmers = read_kmers_from_file(filename)  # read the k-mers from the file
adj_list = Overlap(kmers)  # Construct the overlap graph (adjacency list)
graph_str = adj_list_to_string(adj_list)
# Convert the adjacency list to a string representation

print(graph_str)
pyperclip.copy(graph_str)  # Copy the result to the clipboard


# simple Test case
# test = ["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT"]
# overlap_graph = Overlap(test)


import networkx as nx
import matplotlib.pyplot as plt

testseq = ["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT"]


def construct_overlap_network(Patterns):
    G = nx.DiGraph()
    """on va faire un graphe dirigé pour reconstuire un chemin entre les k-mers tels que suffixe n = préfixe n-1"""
    G.add_nodes_from(Patterns)
    """Construct the overlap graph of a collection of k-mers.

    :param Patterns: A collection Patterns of k-mers.
    :return: The overlap graph Overlap(Patterns), in the form of an adjacency list.
    """

    # Iterate over each k-mer in Patterns
    for i, Pattern in enumerate(Patterns):
        # i is the index of the current k-mer in Patterns ; Pattern is the current k-mer
        # Iterate over each k-mer in Patterns
        for j, Pattern_prime in enumerate(Patterns):
            # j is the index of the current k-mer in Patterns ; Pattern_prime is the current k-mer
            # Skip the current k-mer
            if i == j:
                # if the index of the current k-mer is equal to the index of the current k-mer
                continue  # skip the current k-mer

            # Check if Suffix(Pattern) is equal to Prefix(Pattern_prime)
            if Suffix(Pattern) == Prefix(Pattern_prime):
                G.add_edge(Pattern, Pattern_prime)

    return G


G = construct_overlap_network(testseq)

# visualisation, avec pos des noeuds
fig = plt.figure(figsize=(10, 5))  # create a figure
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(  # draw the graph G
    G,
    pos,
    with_labels=True,
    node_color="red",
    node_size=1500,
    arrowsize=50,
    font_size=8,
    font_weight="bold",
)
plt.savefig("Devoir/Images/03_fig1.png")  # save the figure
plt.show()  # show the figure

# print edges
print("\nEdges in the graph:")
for edge in G.edges():
    print(f"{edge[0]} -> {edge[1]}")

###other graph: too large to be displayed correctly
""" 
kmers = read_kmers_from_file(filename)  # read the k-mers from the file
G = construct_overlap_network(kmers)

# visualisation, avec pos des noeuds
fig = plt.figure(figsize=(10, 5))
pos = nx.spring_layout(G)
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color="red",
    node_size=1500,
    arrowsize=50,
    font_size=8,
    font_weight="bold",
)
plt.show()

# You can also print edges
print("\nEdges in the graph:")
for edge in G.edges():
    print(f"{edge[0]} -> {edge[1]}")
plt.savefig("fig.png")
"""
