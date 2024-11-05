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

from script05 import DeBruijn
from script07 import EulerianPath
from script02 import genome_path_string


def StringReconstruction(filename):
    """Reconstruct a string from its k-mer composition."""

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

    data = read_TextandK_from_file(filename)
    k = data["k"]
    Text = data["Text"]
    Patterns = [Text[i : i + k] for i in range(len(Text) - k + 1)]
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
