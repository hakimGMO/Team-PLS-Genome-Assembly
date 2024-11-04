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

from script03 import read_kmers_from_file, adj_list_to_string
from script05 import DeBruijn
from script07 import EulerianPath
from script02 import genome_path_string


def StringReconstruction(filename):
    filename = "Devoir/Datasets/05_dataset.txt"  #  file path
    kmers = read_kmers_from_file(filename)  # read the k-mers from the file
    adj_list = DeBruijn(kmers)  # Construct the overlap graph (adjacency list)
    Patterns = adj_list_to_string(adj_list)
    # construct the de Bruijn graph
    dB = DeBruijn(Patterns)
    # find an Eulerian path in the de Bruijn graph
    path = EulerianPath(dB)
    # reconstruct the string from the path
    Text = genome_path_string(path)
    return Text


# Example usage
filename = "Devoir/Datasets/08_dataset.txt"
print(StringReconstruction(filename))
