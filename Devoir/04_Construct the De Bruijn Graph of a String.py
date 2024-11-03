# Construct the De Bruijn Graph of a String
"""Given a genome Text, PathGraphk(Text) is the path consisting of |Text| - k + 1 edges, where the i-th edge of this path is labeled by the i-th k-mer in Text and the i-th node of the path is labeled by the i-th (k - 1)-mer in Text. 
The de Bruijn graph DeBruijnk(Text) is formed by gluing identically labeled nodes in PathGraphk(Text).

De Bruijn Graph from a String Problem
Construct the de Bruijn graph of a string.

Given: An integer k and a string Text.

Return:DeBruijnk(Text), in the form of an adjacency list."""

import pyperclip  # to copy the result to the clipboard
import networkx as nx
import matplotlib.pyplot as plt


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


# Test the PathGraphk function
k1 = 4  # length of k-mers
text1 = "AAGATTCTCTAC"  # genome Text

print(PathGraphk(text1, k1))


def DeBruijnk(Text, k):
    """
    Generate the adjacency list of the de Bruijn graph from a genome Text.

    The de Bruijn graph DeBruijnk(Text) is formed by gluing identically labeled nodes in PathGraphk(Text).

    :param Text: A string representing the genome.
    :param k: An integer representing the length of k-mers.

    :return: A dictionary representing the adjacency list of the de Bruijn graph.
    """
    # Generate the nodes and edges of the path graph nodes,
    edges = PathGraphk(Text, k)

    # Initialize an empty dictionary to store the adjacency list
    adj_list = {}

    # Iterate over each edge in the edges list
    for i in range(len(edges[1])):  # edges[1] is the list of k-mers
        edge = edges[1][i]  # get the i-th k-mer
        # Get the prefix of the edge
        prefix = edge[: k - 1]
        # Get the suffix of the edge
        suffix = edge[1:]

        # If the prefix is not in the adjacency list, add it
        if prefix not in adj_list:
            adj_list[prefix] = []

        # Add the suffix to the adjacency list for the prefix
        adj_list[prefix].append(suffix)

    return adj_list


# Test the DeBruijnk function
result = DeBruijnk(text1, k1)
print(result)


def DeBruijnk_tostring(Text, k):
    """
    Convert the adjacency list of the de Bruijn graph to a string representation.

    :param Text: A string representing the genome.
    :param k: An integer representing the length of k-mers.

    :return: A string representation of the de Bruijn graph.
    """
    # Generate the adjacency list using DeBruijnk function
    adj_list = DeBruijnk(Text, k)

    # Initialize an empty string to store the string representation
    graph_string = ""

    # Iterate over each key-value pair in the adjacency list
    for key in sorted(adj_list.keys()):  # sort the keys in the adjacency list
        # Add the key to the string
        graph_string += key + " -> "
        # Add the sorted values to the string
        graph_string += ",".join(sorted(adj_list[key]))
        # Add a newline character
        graph_string += "\n"

    return graph_string


# Test the DeBruijnk_tostring function
print(DeBruijnk_tostring(text1, k1))


def read_TextandK_from_file(filename):
    """
    Read a sequence from a text file.

    :param filename: The path to the file containing the sequence.
    :return: A dictionary containing 'k' and 'Text'.
    """
    with open(filename, "r") as file:
        lines = file.readlines()
        k = int(lines[0].strip())  # read the first line as an integer
        Text = lines[1].strip()  # read the second line as a string

    return {"k": k, "Text": Text}


testseq = read_TextandK_from_file("Devoir/Datasets/04_dataset.txt")
print(testseq)


# Apply the DeBruijnk_tostring function to the test sequence
# Output: A string representation of the de Bruijn graph.
result = DeBruijnk_tostring(testseq["Text"], testseq["k"])

pyperclip.copy(result)


# Visualize the de Bruijn graph using NetworkX and Matplotlib
def nx_debruijn(adj_list, graph_name="De Bruijn Graph"):
    """
    Visualize the de Bruijn graph using NetworkX and Matplotlib.

    :param adj_list: A dictionary representing the adjacency list of the de Bruijn graph.
    :param graph_name: A string representing the name of the graph.
    """
    G = nx.DiGraph()  # directed graph
    edge_labels = {}  # added later to visualize edges with labels

    # Add edges to the graph
    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
            edge_labels[(node, neighbor)] = node + neighbor[-1]

    # Set up the plot
    plt.figure(figsize=(10, 10), dpi=100)
    pos = nx.circular_layout(G)

    # Draw the nodes, edges, and labels
    nx.draw_networkx_nodes(G, pos, node_color="lightblue", node_size=500, alpha=0.6)
    nx.draw_networkx_edges(G, pos, edge_color="gray", arrowsize=15, alpha=0.4)
    nx.draw_networkx_labels(G, pos, font_size=8)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)

    # Set the title and axis
    plt.title(graph_name)
    plt.axis("off")
    # Save the image to the Images folder with the graph name
    plt.savefig(f"Devoir/Images/04_{graph_name.replace(' ', '_')}.png", dpi=300)

    plt.show()


# Test the nx_debruijn function

""" 
#too many nodes to visualize
testseq = read_TextandK_from_file("Devoir/Datasets/04_dataset.txt")
seq_adj_list = DeBruijnk(testseq["Text"], testseq["k"])
nx_debruijn(seq_adj_list) """

# Test with a smaller sequence
# The sequence in the Book is "TAATGCCATGGGATGTT" and k=3

adj_list_test_Book = DeBruijnk("TAATGCCATGGGATGTT", 3)  # generate the adjacency list
print(adj_list_test_Book)

# Visualize the de Bruijn graph for the Book sequence
nx_debruijn(
    adj_list_test_Book, graph_name="De Bruijn Graph for TAATGCCATGGGATGTT with k=3"
)
