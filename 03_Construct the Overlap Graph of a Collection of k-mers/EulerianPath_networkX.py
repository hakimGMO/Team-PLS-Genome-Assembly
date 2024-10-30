import matplotlib.pyplot as plt
import networkx as nx
"""
les outputs
Cycle eulérien du graphe 0->3->2->6->8->7->9->6->5->4->2->1->0
ce graphe est eulerien:  True
ce graphe a un chemin eulerien:  True
Chemin eulerien comme liste de tuples: [(0, 3), (3, 2), (2, 6), (6, 8), (8, 7), (7, 9), (9, 6), (6, 5), (5, 4), (4, 2), (2, 1), (1, 0)]
Chemin eulerien: 0 -> 3 -> 2 -> 6 -> 8 -> 7 -> 9 -> 6 -> 5 -> 4 -> 2 -> 1 -> 0
"""

# plus simple bia Nx

input1 = {
    0: [3], 1: [0], 2: [1, 6], 3: [2], 4: [2],
    5: [4], 6: [5, 8], 7: [9], 8: [7], 9: [6]
}

graphe = input1

def cycle_eulerien(graphe):
    G = nx.DiGraph(graphe)
    # cycle eulérien via eulerian_circuit de Nx
    cycle = list(nx.eulerian_circuit(G))
    # Convertir la liste d'arêtes en liste de noeuds
    Cycle = [cycle[0][0]]
    for edge in cycle:
        Cycle.append(edge[1])
    return Cycle

def chemin_eulerien(graphe):
    G = nx.DiGraph(graphe)
    # chemin eulérien via eulerian_path de Nx
    path = list(nx.eulerian_path(G))
    # Convertir la liste d'arêtes en liste de noeuds
    chemin = [path[0][0]]
    for edge in path:
        chemin.append(edge[1])
    return chemin


cycle = cycle_eulerien(graphe)
print("Cycle eulérien du graphe", '->'.join(str(x) for x in cycle))


# Option: visualiser le graphe
# def Nx_graphe(graphe):
    # G = nx.DiGraph(graphe)
    # plt.savefig('EulerianPath_Nx.png')
    # pos = nx.planar_layout(G)
    # nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, arrowsize=10, edgelist=path)
    # plt.show()



def chemin_eulerien(graphe):
    G = nx.DiGraph(graphe)
    # return [u for u, v in nx.eulerian_path(G)] + [list(nx.eulerian_path(G))[-1][1]]
    pos = nx.planar_layout(G)
    path = list(nx.eulerian_path(G)) # On recupere les tuplets source/destination
    print("ce graphe est eulerien: ", nx.is_eulerian(G))
    print("ce graphe a un chemin eulerien: ", nx.has_eulerian_path(G))
    print(f"Chemin eulerien comme liste de tuples: {path}")
    print("Chemin eulerien:", ' -> '.join(str(node) for node, _ in path + [(path[-1][1], None)]))
    # on affiche les noeuds dans l'ordre en ignorant la destination de chaque arete ( _ in)
    # (path[-1][1], None)] pour inclure le dernier noeud
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, arrowsize=10, edgelist=path)
    # plt.show()

chemin_eulerien(graphe)


# Nx_graphe(graphe)


# plt affiche toujours le cycle et non le chemin eulérien !!!!
