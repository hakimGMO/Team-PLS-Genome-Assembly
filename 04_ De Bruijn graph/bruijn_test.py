import networkx as nx
import matplotlib.pyplot as plt


# parametres
k = 4
text = "AAGATTCTCTAC"


def de_bruijn(k, text):
    # Créer le graphe dirigé
    G = nx.DiGraph()
    # Construire le graphe avec noeud source = prefixe et noeud destinataire = suffixe.
    # l'arete entre neoud source et destination, permet de ne pas creer les noeuds
    for i in range(len(text) - k + 1):
        kmer = text[i : i + k]
        prefix = kmer[:-1]
        suffix = kmer[1:]
        G.add_edge(
            prefix, suffix
        )  # declarer une arete permet de creer les noeuds automatiquement

    # affichage liste d'adjacence
    for node in sorted(G.nodes()):
        successors = sorted(
            G.neighbors(node)
        )  # on recup les neouds suivants, par ordre alpha
        print(f"{node} -> {','.join(successors)}")


de_bruijn(k, text)
