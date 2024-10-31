def afficher_statistiques(patterns, graph, path, sequence):
    """
    Affiche les statistiques principales du graphe et de la séquence
    """
    print("\nStatistiques :")
    print("-" * 50)

    # Statistiques sur les k-mers d'entrée
    print(f"Nombre de k-mers en entrée : {len(patterns)}")
    print(f"Longueur de chaque k-mer : {len(patterns[0])}")

    # Statistiques sur le graphe
    noeuds = set(list(graph.keys()) + [item for sublist in graph.values() for item in sublist])
    print(f"\nNombre de nœuds dans le graphe : {len(noeuds)}")
    print(f"Nombre d'arêtes dans le graphe : {sum(len(v) for v in graph.values())}")

    # Statistiques sur le chemin
    print(f"\nLongueur du chemin eulérien : {len(path)}")
    print(f"Premier nœud du chemin : {path[0]}")
    print(f"Dernier nœud du chemin : {path[-1]}")

    # Statistiques sur la séquence reconstruite
    print(f"\nLongueur de la séquence reconstruite : {len(sequence)}")
    print(f"Début de la séquence : {sequence[:50]}...")
    print(f"Fin de la séquence : ...{sequence[-50:]}")


# Test pour les deux jeux de données
if __name__ == "__main__":
    # Test avec le petit exemple
    print("Test avec le petit exemple :")
    patterns = [
        "CTTA",
        "ACCA",
        "TACC",
        "GGCT",
        "GCTT",
        "TTAC"
    ]

    # Création du graphe et reconstruction
    graph = create_graph(patterns)
    path = find_path(graph)
    result = path_to_string(path)

    # Affichage des statistiques
    afficher_statistiques(patterns, graph, path, result)

    # Test avec le grand jeu de données
    print("\n\nTest avec le grand jeu de données :")
    try:
        patterns_large = read_kmers_from_file('extra_dataset')
        graph_large = create_graph(patterns_large)
        path_large = find_path(graph_large)
        result_large = path_to_string(path_large)

        # Affichage des statistiques
        afficher_statistiques(patterns_large, graph_large, path_large, result_large)

    except FileNotFoundError:
        print("Le fichier 'extra_dataset' n'a pas été trouvé.")