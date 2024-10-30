import matplotlib.pyplot as plt
import networkx as nx
"""
je mets l'input sous format de dict

les outputs:
ce graphe est eulerien:  False
ce graphe a un chemin eulerien:  True
Chemin eulerien comme liste de tuples: [(6, 7), (7, 8), (8, 9), (9, 6), (6, 3), (3, 0), (0, 2), (2, 1), (1, 3), (3, 4)]
Chemin eulerien: 6 -> 7 -> 8 -> 9 -> 6 -> 3 -> 0 -> 2 -> 1 -> 3 -> 4
"""

# plus simple via Nx

input1 = {
    0: [2], 1: [3], 2: [1], 3: [0, 4],
    6: [3, 7], 7: [8], 8: [9], 9: [6]
}


graphe = input1
def chemin_eulerien(graphe):
    G = nx.DiGraph(graphe)
    path = list(nx.eulerian_path(G)) # On recupere les tuplets source/destination
    print("ce graphe est eulerien: ", nx.is_eulerian(G))
    print("ce graphe a un chemin eulerien: ", nx.has_eulerian_path(G))
    print(f"Chemin eulerien comme liste de tuples: {path}")
    print("Chemin eulerien:", ' -> '.join(str(node) for node, _ in path + [(path[-1][1], None)]))
    # on affiche les noeuds dans l'ordre en ignorant la destination de chaque arete ( _ in)
    # (path[-1][1], None)] pour inclure le dernier noeud
    pos = nx.circular_layout(G)
    nx.draw_networkx_edges(G, pos, edge_color='blue', arrows=True, arrowsize=15)
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
    nx.draw_networkx_labels(G, pos)
    plt.title("recherche de chemin eulerien_input1")
    plt.axis('off')
    plt.savefig("chemin eulerien_Nx.png")
    plt.show()

result = chemin_eulerien(graphe)

