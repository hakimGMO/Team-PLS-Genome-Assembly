"""
DeBruijn(Patterns) :
- Prend les k-mers en entrée
- Crée le graphe de DeBruijn
- Retourne la structure du graphe

find_start_node(graphe):
- Calcule les degrés entrants et sortants de chaque nœud
- Trouve un nœud approprié pour commencer le chemin eulérien

EulerianPath(graphe) :
- Prend le graphe en entrée
- Trouve un chemin qui utilise chaque arête une fois
- Retourne la liste des nœuds visités

PathToGenome(path) :
- Prend le chemin en entrée
- Reconstruit la séquence
- Retourne la chaîne finale

StringReconstruction(Patterns)
- reprend les 3 fonctions précédentes.
"""


def DeBruijn(patterns):
    """
    Construit le graphe de DeBruijn à partir des k-mers.
    Retourne un dico où les clés sont les nœuds=préfixes
    et les valeurs sont les listes des nœuds connectés=suffixes
    """
    graph = {}
    for pattern in patterns:
        prefix = pattern[:-1]
        suffix = pattern[1:]
        if prefix not in graph:
            graph[prefix] = []
        graph[prefix].append(suffix)
    return graph


def find_start_node(graph):
    """
    Trouve le nœud de départ approprié pour le chemin eulérien.
    """
    # Compter les degrés entrants et sortants
    in_degrees = {}
    out_degrees = {}

    # Initialiser les degrés sortants
    for node in graph:
        out_degrees[node] = len(graph[node])
        for neighbor in graph[node]:
            if neighbor not in in_degrees:
                in_degrees[neighbor] = 0
            in_degrees[neighbor] = in_degrees.get(neighbor, 0) + 1

    # Trouver un nœud qui a un degré sortant supérieur au degré entrant
    for node in graph:
        out_deg = out_degrees.get(node, 0)
        in_deg = in_degrees.get(node, 0)
        if out_deg > in_deg:
            return node

    # Si aucun nœud n'est trouvé, prendre le premier nœud avec des arêtes sortantes
    return list(graph.keys())[0]


def EulerianPath(graph):
    """
    Trouve un chemin eulérien dans le graphe.
    """
    # Créer une copie du graphe pour ne pas le modifier
    graph = {k: v[:] for k, v in graph.items()}

    # Trouver le nœud de départ approprié
    start = find_start_node(graph)

    path = []
    stack = [start]

    while stack:
        current = stack[-1]

        if current in graph and graph[current]:
            # S'il y a des arêtes non visitées, prendre la première
            next_node = graph[current].pop(0)
            stack.append(next_node)
        else:
            # Si plus d'arêtes, ajouter le nœud au chemin
            path.append(stack.pop())

    # Inverser le chemin car nous l'avons construit à l'envers
    return path[::-1]


def PathToGenome(path):
    """
    Convertit un chemin en une séquence.
    Le premier nœud est pris en entier, puis on ajoute
    le dernier caractère de chaque nœud suivant.
    """
    if not path:
        return ""

    # Commencer avec le premier nœud
    text = path[0]

    # Ajouter le dernier caractère de chaque nœud suivant
    for node in path[1:]:
        text += node[-1]

    return text


def StringReconstruction(patterns):
    """
    Fonction principale pour reconstruire notre séquence à partir de patterns de k-mers.
    """
    dB = DeBruijn(patterns)
    path = EulerianPath(dB)
    text = PathToGenome(path)
    return text


def read_kmers_from_file(extra_dataset):
    """
    Pour parser l'extradataset
    """
    with open(extra_dataset, 'r') as file:
        # lit toutes les lignes et enlève les espaces/retours à la ligne superflus
        kmers = [line.strip() for line in file if line.strip()]
    return kmers


# les differents inputs de rosalind
input1 = [
        "CTTA",
        "ACCA",
        "TACC",
        "GGCT",
        "GCTT",
        "TTAC"
        ]

input2 = read_kmers_from_file('extra_dataset')  # Assurez-vous que le fichier est dans le même dossier


patterns = input2
result = StringReconstruction(patterns)

print(f"Patterns d'entrée : {patterns}")
print(f"Séquence reconstruite : {result}")
