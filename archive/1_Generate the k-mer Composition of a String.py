#Generate the k-mer Composition of a String

""" Given a string Text, its k-mer composition Compositionk(Text) is the collection of all k-mer substrings of Text (including repeated k-mers). 
For example,

Composition3(TATGGGGTGC) = {ATG, GGG, GGG, GGT, GTG, TAT, TGC, TGG}
Note that we have listed k-mers in lexicographic order (i.e., how they would appear in a dictionary)
rather than in the order of their appearance in TATGGGGTGC. We have done this because the correct ordering of the reads is unknown when they are generated.

String Composition Problem
Generate the k-mer composition of a string.

Given: An integer k and a string Text.

Return: Compositionk(Text) (the k-mers can be provided in any order).

Sample Dataset 
5
CAATCCAAC

Sample Output
AATCC
ATCCA
CAATC
CCAAC
TCCAA"""

def Compositionk(Text, k):
    kmers = []
    for i in range(len(Text)-k+1):
        kmers.append(Text[i:i+k])
    return kmers