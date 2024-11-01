def genome_path_string(kmers):
    """Reconstruct a string from its genome path.

    Input: A sequence path of k-mers Pattern1, … ,Patternn such that the last k - 1 symbols of Patterni are equal to the first k-1 symbols of Patterni+1 for 1 ≤ i ≤ n-1.
    Output: A string Text of length k+n-1 such that the i-th k-mer in Text is equal to Patterni (for 1 ≤ i ≤ n).
    """
    # Start with the first k-mer
    genome_string = kmers[0]

    # Append the last character of each subsequent k-mer
    for kmer in kmers[1:]:
        genome_string += kmer[-1]

    return genome_string
