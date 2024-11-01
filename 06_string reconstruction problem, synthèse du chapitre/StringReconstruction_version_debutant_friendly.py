def create_graph(patterns):
    """
    Crée un graphe simple à partir des k-mers.
    Exemple: pour "ATG", crée une connexion de "AT" vers "TG"
    """
    graph = {}

    for kmer in patterns:
        # Prend les 3 premières lettres de CTTA -> CTT
        start = kmer[:-1]
        # Prend les 3 dernières lettres de CTTA -> TTA
        end = kmer[1:]

        # Si on n'a jamais vu ce début, on crée une liste vide
        if start not in graph:
            graph[start] = []

        # On ajoute la fin à la liste des connexions
        graph[start].append(end)

    return graph


def find_start(graph):
    """
    Trouve par quel nœud commencer dans le graphe.
    Compte combien de fois chaque nœud apparaît au début et à la fin.
    """
    # Compte combien de fois chaque nœud a des flèches qui en partent
    outgoing = {}
    # Compte combien de fois chaque nœud a des flèches qui y arrivent
    incoming = {}

    # On compte les flèches
    for node in graph:
        # Compte les flèches qui partent
        outgoing[node] = len(graph[node])

        # Compte les flèches qui arrivent
        for next_node in graph[node]:
            if next_node not in incoming:
                incoming[next_node] = 0
            incoming[next_node] = incoming.get(next_node, 0) + 1

    # On cherche un nœud qui a plus de départs que d'arrivées
    for node in graph:
        out_edges = outgoing.get(node, 0)
        in_edges = incoming.get(node, 0)
        if out_edges > in_edges:
            return node

    # Si on n'en trouve pas, on prend le premier nœud du graphe
    return list(graph.keys())[0]


def find_path(graph):
    """
    Trouve un chemin qui passe par toutes les connexions une seule fois.
    """
    # On fait une copie du graphe pour pouvoir le modifier
    graph_copy = {}
    for start, ends in graph.items():
        graph_copy[start] = ends.copy()

    # On commence par le bon nœud de départ
    start = find_start(graph_copy)

    path = []
    nodes_to_visit = [start]

    # Tant qu'il reste des nœuds à visiter
    while nodes_to_visit:
        current_node = nodes_to_visit[-1]

        # S'il reste des connexions non utilisées depuis ce nœud
        if current_node in graph_copy and graph_copy[current_node]:
            next_node = graph_copy[current_node].pop(0)
            nodes_to_visit.append(next_node)
        else:
            # Si plus de connexions, on ajoute ce nœud au chemin
            path.append(nodes_to_visit.pop())

    # On inverse le chemin car on l'a construit à l'envers
    return path[::-1]


def path_to_string(path):
    """
    Reconstruit la séquence finale à partir du chemin trouvé.
    """
    if not path:
        return ""

    # On commence avec le premier morceau
    text = path[0]

    # Pour chaque morceau suivant, on ajoute sa dernière lettre
    for piece in path[1:]:
        text += piece[-1]

    return text


def reconstruct_string(patterns):
    """
    Fonction principale qui reconstruit la séquence complète.
    """
    graph = create_graph(patterns)
    path = find_path(graph)
    text = path_to_string(path)
    return text

def read_kmers_from_file(extra_dataset):
    """
    Pour parser l'extradataset
    """
    with open(extra_dataset, 'r') as file:
        # lit toutes les lignes et enlève les espaces/retours à la ligne superflus
        kmers = [line.strip() for line in file if line.strip()]
    return kmers

# Test avec l'exemple
patterns = [
    "CTTA",
    "ACCA",
    "TACC",
    "GGCT",
    "GCTT",
    "TTAC"
]

input2 = read_kmers_from_file('extra_dataset_readpairs')  # Assurez-vous que le fichier est dans le même dossier
patterns = input2
result = reconstruct_string(patterns)

# On reconstruit la séquence
result = reconstruct_string(patterns)
print(f"K-mers d'entrée : {patterns}")
print(f"Séquence reconstruite : {result}")

# tests stats à partir du script
from tests_stastistiques_sequence import afficher_statistiques

graph = create_graph(patterns)
path = find_path(graph)
text = path_to_string(path)
afficher_statistiques(patterns, graph, path, result)

# fin :)