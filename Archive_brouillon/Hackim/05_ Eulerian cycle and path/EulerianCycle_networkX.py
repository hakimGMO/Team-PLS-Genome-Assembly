import matplotlib.pyplot as plt  # Importing matplotlib library
import networkx as nx  # Importing networkx library

# Other option: via networkx
# We use the networkx library to find the Eulerian cycle in a directed graph.
# plus simple via Nx

# Example
input1 = {
    0: [3],
    1: [0],
    2: [1, 6],
    3: [2],
    4: [2],
    5: [4],
    6: [5, 8],
    7: [9],
    8: [7],
    9: [6],
}

graphe = input1


def cycle_eulerien(graphe):
    """Trouve un cycle eulérien dans un graphe."""
    G = nx.DiGraph(graphe)
    # cycle eulérien via eulerian_circuit de Nx
    cycle = list(nx.eulerian_circuit(G))
    # Convertir la liste d'arêtes en liste de noeuds
    chemin = [cycle[0][0]]
    for edge in cycle:
        chemin.append(edge[1])
    return chemin


# Exemple
cycle = cycle_eulerien(graphe)
print("->".join(str(x) for x in cycle))


# Option: visualiser le graphe
def visualiser_graphe(graphe):
    pos = nx.circular_layout(graphe)
    G = nx.DiGraph(graphe)
    nx.draw(
        G, pos, with_labels=True, node_color="lightblue", node_size=500, arrowsize=20
    )
    # plt.show()
    # plt.savefig('EulerianCycle_Nx.png')
    print("This graph is eulerian: ", nx.is_eulerian(G))
    print("This graph has eulerian path: ", nx.has_eulerian_path(G))
    path = list(nx.eulerian_path(G))
    print(path)
    # print("Eulerian path:", ' -> '.join(str(node) for node, _ in path + [(path[-1][1], None)]))


visualiser_graphe(graphe)
