import networkx as nx
import matplotlib.pyplot as plt

# parametres rosalind

k1 = 3
k2 = 10
text1 = "AAGATTCTCTAC"
text2 = "CTGAAGACCTCTCCACATTACTACGATATAAATCATTTCAGCCTCTAGATACGCCTTGGTGGGTGGGGTTGGCAATTTACGATATGTCCGAATGATTTGACACCAAATACCTTAGCTAGCCCCAAGGAAAATTCTGGGCTTTACGTTGGCCGAGCCACATTACTACAGTAAGGTTAAGCAACCAGCCAGTCGCTCATAAGGACTCCACGCCTCCCGTTACTGACTTCCAACAACAATGTGACAGTAGACTGGAACCTGGGAGGACATTATTGATTCGCCGCGAATCTTCTAAGGTATTTTACCCCCACTGGTCACCTTAACCATTAAGACCTCGAAGTGACACCTAGCCTCTTAACACCCAACTCCACCGACAATACCTATTCGCTGACAAGCGGGACATCCGATCGCCCCTGACTCGAGGTGTCTACCGTCCATCGATTGCTAAACTTTGTTAGGAGTCTAAGCGAACCATGGGAAGGGGGCGGCAGTCAACGTGCTCCTTTAGTGAGGTACCATATTCTTACAGCATGTGGAGCGCAGCAAACTAGCGACCGGGAGTACTCCCACAACCCTGGGTACGTACTGCACTTTTTTCAAGAGCCAGGGTCATTTAAATAGCATCTTTGCTCTTTCTGATAAGGGGGCGACCATCTCCGAATTGAGCCAAACGCTGGTATAAGACTCGTCTCATGACTCCCTAGCCATTTGTATGTTGTCATTTCTGATTTTAGCAGGTAAAACGTAAGGCCTGCTAAAGAATCACGCGGGGAGGCCTTAAATTTCGTCATGGAGCAATCGTCCTAGATTGCTGTGAAGGTTCGTACCAGTAGAGTCTAATGTGCGTAAATGTTAACTGGCCGTATATTCTCTGGTGAGCTGAAACAGAAAGCTGGCAGAAAGCCACTCTTGCTGTTTCGTGTGTACGGACATCGGGATAGTACCAAAAAGCATGTTCTTCATCTGGCGATGCTTGATGTCTACCGTAGACACCTTCATACGT"
text3 = "TAATGCCATGGGATGTT"
text4 = "TAATGGGATGCCATGTT"
text = text4
k = k1

def path_graph_k(text, k):
    # nœuds (k-1 mers, comme indiqué dans le txt)
    nodes = [text[i:i + k - 1] for i in range(len(text) - k + 2)]
    # arêtes (k-mers)
    edges = [text[i:i + k] for i in range(len(text) - k + 1)]
    return nodes, edges


def debruijn_k(text, k):
    # PathGraph
    nodes, edges = path_graph_k(text, k)

    # liste d'adjacence en "collant les nœuds identiques"
    adj_list = {}

    for i in range(len(edges)):
        prefix = edges[i][:k - 1]
        suffix = edges[i][1:]

        if prefix not in adj_list:
            adj_list[prefix] = []
        if suffix not in adj_list[prefix]:
            adj_list[prefix].append(suffix)

    return adj_list


# visualisation du graph de debruijn avec nx et plt, list d'ajacence en input
def nx_debruijn(adj_list):
    G = nx.DiGraph()
    edge_labels = {} #rajouté a posteriori pour visualiser les aretes avec labels

    for node, neighbors in adj_list.items():
        for neighbor in neighbors:
            G.add_edge(node, neighbor)
            edge_labels[(node, neighbor)] = node + neighbor[-1]

    plt.figure(figsize=(10, 10), dpi=100)
    pos = nx.circular_layout(G)

    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500, alpha=0.6)
    nx.draw_networkx_edges(G, pos, edge_color='gray', arrowsize=15, alpha=0.4)
    nx.draw_networkx_labels(G, pos, font_size=8)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=6)

    plt.title(f"Graphe de De Bruijn")
    plt.axis('off')
    plt.savefig('debruijn_graph_text4_k=3.png', dpi=300)
    plt.show()

result = debruijn_k(text, k)
nx_debruijn(result)


for node in sorted(result):
    print(f"{node} -> {','.join(sorted(result[node]))}")
for edge in sorted(result):
    print(f"{edge} -> {','.join(sorted(result[edge]))}")