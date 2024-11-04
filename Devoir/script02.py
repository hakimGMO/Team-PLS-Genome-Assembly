import pyperclip  # Import the pyperclip module for copying the result to the clipboard


def genome_path_string(kmers):
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


# Test
list_kmers = [
    "ACCGA",
    "CCGAA",
    "CGAAG",
    "GAAGC",
    "AAGCT",
]  # sequence path of k-mers need to be in order
result = genome_path_string(list_kmers)
print(result)  # ACCGAAGCT


# from file
def genome_path_string_from_file(file_path):
    """Reconstruct a string from its genome path.
    Input: format file.text
    : A sequence path of k-mers Pattern1, … ,Patternn such that the last k - 1 symbols of Patterni are equal to the first k-1 symbols of Patterni+1 for 1 ≤ i ≤ n-1.
    all k-mers are in order ; one per line ; no empty line ;
    Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni (for 1 ≤ i ≤ n).
    """
    # Open the file and read all lines
    with open(file_path, "r") as file:
        lines = file.readlines()

    # Remove spaces and newline characters
    kmers = [line.strip() for line in lines]

    # Check if there are any k-mers in the file
    if not kmers:
        return ""

    # Construct the genome string from the k-mers
    genome_string = kmers[0]

    for kmer in kmers[1:]:
        genome_string += kmer[-1]

    return genome_string


result2 = genome_path_string_from_file("Devoir/Datasets/02_dataset.txt")
print(result2)

pyperclip.copy(result2)  # Copy the result to the clipboard
