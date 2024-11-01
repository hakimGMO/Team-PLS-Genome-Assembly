def Compositionk(Text, k):
    """Generate the k-mer composition of a string.
    Text: A string.
    k: An integer."""
    kmers = []  # create an empty list to store the k-mers
    for i in range(len(Text) - k + 1):  # iterate over the string
        kmers.append(Text[i : i + k])  # add the k-mer to the list
    return sorted(kmers)  # return the list of k-mers sorted in lexicographic order


# Test the function with the sample dataset
Text = "CAATCCAAC"
k = 5
print(Compositionk(Text, k))  # ['AATCC', 'ATCCA', 'CAATC', 'CCAAC', 'TCCAA']
