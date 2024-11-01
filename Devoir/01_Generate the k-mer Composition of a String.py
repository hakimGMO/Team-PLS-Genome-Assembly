def Compositionk(Text, k):
    """Generate the k-mer composition of a string.
    Text: A string.
    k: An integer."""
    kmers = []  # create an empty list to store the k-mers
    for i in range(len(Text) - k + 1):  # iterate over the string
        # +1 is added to len(Text) - k to include the last k-mer in the string
        kmers.append(Text[i : i + k])  # add the k-mer to the list
    return sorted(kmers)  # return the list of k-mers sorted in lexicographic order


# Test the function with the sample dataset
Text = "CAATCCAAC"
k = 5
print(Compositionk(Text, k))  # ['AATCC', 'ATCCA', 'CAATC', 'CCAAC', 'TCCAA']
print(
    Compositionk(
        "CTATCATTAGGTTGATGGAGATGGCAACCTGGCCGATTTCAATGCAATCCGTTACTTACAATGCATTTCCTGGCGTCTGATTAATAGCCACTGGGGCTTGTATACACATCAAAGGTGGCGCCATCGGTAGGCGTCGGACGTTAGTAACTCTCGGTTCCGGACGTGATAACGGCCGTATAAAACTGCTACCACACTTAGATGGAGTCGACGTATAATCGCAAGTATAGGCGTTTTGTGGGTTCTCGAAAGCGGCCTGTGGTCCTGAATTTCATACCTATCTCGAAGCGGCTGATCGTACGTTACCGGGTCAGTTCCCGGTTGTTTCTGTTACTTAGTATCCAACCACACATAAATATCCATTTCAATTTTATGAAGCTGTTTACTTGGATCACTCTGGGGGGCTGTTTGCCTCGCACTCAACGGAGAAAGCTAGCGCTTCGTATCTGATTAAACTCAAACACTTAACCTGACCTCTGGAGTGGAGTTTAACATACGCAATAAGGAAATCCCATACATGTGAAACGTCAACAACCTGGGTATGCTGTATTAAAACACTGTATAAGCAGACTAGAGCGCCAGAACCTTTATAGGGGTTCATAGATTCCTATGCGGGTGACGCATGTGAAAGAATCGGTTGGCTATCCCCACTACGGTGCCTCGGTTCTATCCCCAGCAGTTGACGATCAGAAAGCGACATTCTCTTTTGCCCCTACGCGACAGTCCGTGAAGCTTAGTCGGCCGGAGATAGCACGGATTGTGTAGACCTAAAACAAGCATCTTGATAATTCACGAGGCAACTTGGAGCGCGGGAAACAACGCCGAAAATGCCGTAATTGCACTTATAAGTCAGAGATGCTACATAGCCCTAGTGCCTAAAGCTGGTGCTGGATGGTTATTGACCTGCATTTCGGTTTTACCTTTTAATTGGGCACGAACCTGTAGATTTCCCCCTCACAGGTGCTAAAATATTTCGTATACCTAGCTAATTTGTCCATTTCAC",
        50,
    )
)


def Compositionk(file_path):
    """Generate the k-mer composition of a string from a file.
    file_path: Path to the text file with k on the first line and Text on the second line.
    """

    with open(file_path, "r") as file:
        k = int(file.readline().strip())  # Read k from the first line
        Text = file.readline().strip()  # Read the sequence from the second line

    kmers = []  # Create an empty list to store the k-mers
    for i in range(len(Text) - k + 1):  # Iterate over the string
        kmers.append(Text[i : i + k])  # Add the k-mer to the list

    return "\n".join(sorted(kmers))  # Return sorted k-mers, one per line
