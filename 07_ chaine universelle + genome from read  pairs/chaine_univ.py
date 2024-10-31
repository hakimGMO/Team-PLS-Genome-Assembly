"""
LLM Sonnet : tuto pas à pas pour la création de l'universal string pour k=3
"""
import matplotlib.pyplot as plt
import math
import numpy as np

def exemple_k3():
    """
    Exemple très détaillé de la création d'une chaîne universelle pour k=3
    """
    k = 3
    print(f"\nEXEMPLE DÉTAILLÉ POUR k={k}")
    print("=" * 50)

    # ÉTAPE 1 : Création des k-mers binaires
    print("\n1. CRÉATION DES K-MERS (k=3)")
    print("-" * 30)
    kmers = ['']

    # Construction progressive des k-mers
    print("Construction des k-mers pas à pas :")
    for iteration in range(k):
        nouveaux_kmers = []
        for kmer in kmers:
            nouveaux_kmers.append(kmer + '0')
            nouveaux_kmers.append(kmer + '1')
        kmers = nouveaux_kmers
        print(f"Après itération {iteration + 1}: {kmers}")

    print(f"\nNombre total de k-mers : {len(kmers)}")
    print(f"K-mers finaux : {sorted(kmers)}")

    # ÉTAPE 2 : Création du graphe de De Bruijn
    print("\n2. CRÉATION DU GRAPHE")
    print("-" * 30)
    graphe = {}

    print("Construction du graphe :")
    for kmer in sorted(kmers):
        prefixe = kmer[:-1]  # Deux premiers chiffres
        suffixe = kmer[1:]  # Deux derniers chiffres
        print(f"K-mer {kmer}: préfixe={prefixe}, suffixe={suffixe}")

        if prefixe not in graphe:
            graphe[prefixe] = []
        graphe[prefixe].append(suffixe)

    print("\nStructure finale du graphe :")
    for noeud in sorted(graphe.keys()):
        print(f"Nœud '{noeud}' connecté à : {sorted(graphe[noeud])}")

    # ÉTAPE 3 : Recherche du chemin eulérien
    print("\n3. RECHERCHE DU CHEMIN EULÉRIEN")
    print("-" * 30)

    chemin = []
    noeud_depart = list(sorted(graphe.keys()))[0]
    noeuds_a_visiter = [noeud_depart]
    graphe_copie = {k: sorted(v.copy()) for k, v in graphe.items()}

    print(f"Début au nœud : {noeud_depart}")

    etape = 1
    while noeuds_a_visiter:
        noeud_actuel = noeuds_a_visiter[-1]
        print(f"\nÉtape {etape}:")
        print(f"Nœud actuel : {noeud_actuel}")

        if noeud_actuel in graphe_copie and graphe_copie[noeud_actuel]:
            prochain_noeud = graphe_copie[noeud_actuel].pop(0)
            print(f"→ Avance vers : {prochain_noeud}")
            noeuds_a_visiter.append(prochain_noeud)
        else:
            noeud_ajoute = noeuds_a_visiter.pop()
            chemin.append(noeud_ajoute)
            print(f"← Retour et ajout au chemin : {noeud_ajoute}")
        etape += 1

    chemin = chemin[::-1]
    print(f"\nChemin eulérien final : {chemin}")

    # ÉTAPE 4 : Construction de la chaîne universelle
    print("\n4. CONSTRUCTION DE LA CHAÎNE")
    print("-" * 30)

    resultat = chemin[0]
    print(f"Début avec : {resultat}")

    for noeud in chemin[1:]:
        resultat += noeud[-1]
        print(f"Ajout de '{noeud[-1]}' depuis {noeud} → {resultat}")

    print(f"\nChaîne universelle finale : {resultat}")

    # ÉTAPE 5 : Vérification
    print("\n5. VÉRIFICATION")
    print("-" * 30)
    print("Vérifions que tous les k-mers sont présents :")
    chaine_circulaire = resultat + resultat[:k - 1]
    kmers_trouves = set()

    for i in range(len(resultat)):
        kmer = chaine_circulaire[i:i + k]
        kmers_trouves.add(kmer)
        present = kmer in kmers
        print(f"Position {i}: k-mer {kmer} {'✓' if present else '✗'}")

    print(f"\nNombre de k-mers trouvés : {len(kmers_trouves)}")
    print(f"Tous les k-mers sont présents : {kmers_trouves == set(kmers)}")
    print("\n6. VISUALISATION DU GRAPHE")
    print("-" * 30)
    visualiser_graphe_debruijn(graphe, chemin)


def visualiser_graphe_debruijn(graphe, chemin=None):
    """
    Crée une visualisation du graphe de De Bruijn avec les nœuds aux coins d'un carré
    """
    # Création de la figure
    fig, ax = plt.subplots(figsize=(10, 10), facecolor='white')
    ax.set_facecolor('white')

    # Configuration esthétique
    COULEUR_NOEUD = 'white'
    COULEUR_BORDURE = 'black'
    COULEUR_TEXTE = 'black'
    COULEUR_FLECHE = 'gray'
    COULEUR_CHEMIN = 'red'

    # Positions fixes des nœuds en carré
    positions = {
        '00': (-1, 1),  # Coin supérieur gauche
        '01': (1, 1),  # Coin supérieur droit
        '11': (1, -1),  # Coin inférieur droit
        '10': (-1, -1)  # Coin inférieur gauche
    }

    def dessiner_fleche_courbe(debut, fin, courbure=0.2, couleur=COULEUR_FLECHE, boucle=False):
        """Dessine une flèche courbe entre deux points"""
        x1, y1 = positions[debut]
        x2, y2 = positions[fin]

        if boucle:  # Si c'est une boucle sur le même nœud
            t = np.linspace(0, 2 * np.pi, 100)
            rayon = 0.15
            centre_x = x1 + rayon
            centre_y = y1 + rayon
            xs = centre_x + rayon * np.cos(t)
            ys = centre_y + rayon * np.sin(t)
            plt.plot(xs, ys, color=couleur, linewidth=1.5, zorder=1)
            # Ajouter une flèche sur la boucle
            angle = np.pi / 3
            dx = rayon * np.cos(angle)
            dy = rayon * np.sin(angle)
            plt.arrow(xs[75], ys[75], dx * 0.1, dy * 0.1,
                      head_width=0.05, color=couleur, zorder=1)
        else:
            # Pour les connections normales
            dx = x2 - x1
            dy = y2 - y1

            if abs(dx) + abs(dy) == 4:  # Connection diagonale
                plt.arrow(x1, y1, dx * 0.9, dy * 0.9,
                          head_width=0.1, color=couleur,
                          length_includes_head=True, zorder=1)
            else:  # Connection horizontale ou verticale
                plt.arrow(x1, y1, dx * 0.9, dy * 0.9,
                          head_width=0.1, color=couleur,
                          length_includes_head=True, zorder=1)

    # Dessiner toutes les connexions
    for debut, fins in graphe.items():
        for fin in fins:
            if debut == fin:  # Boucle
                dessiner_fleche_courbe(debut, fin, couleur=COULEUR_FLECHE, boucle=True)
            else:
                dessiner_fleche_courbe(debut, fin, couleur=COULEUR_FLECHE)

    # Dessiner le chemin eulérien si fourni
    if chemin:
        for i in range(len(chemin) - 1):
            debut, fin = chemin[i], chemin[i + 1]
            if debut == fin:
                dessiner_fleche_courbe(debut, fin, couleur=COULEUR_CHEMIN, boucle=True)
            else:
                dessiner_fleche_courbe(debut, fin, couleur=COULEUR_CHEMIN)

    # Dessiner les nœuds
    for noeud, (x, y) in positions.items():
        circle = plt.Circle((x, y), 0.15, facecolor=COULEUR_NOEUD,
                            edgecolor=COULEUR_BORDURE, linewidth=2, zorder=3)
        ax.add_patch(circle)
        plt.text(x, y, noeud, color=COULEUR_TEXTE,
                 horizontalalignment='center',
                 verticalalignment='center',
                 fontweight='bold',
                 fontsize=20,
                 zorder=4)

    # Configuration finale
    plt.title("Universal string k = 4")
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.savefig("Universal string k = 4")
    plt.tight_layout()
    plt.show()

# Exécution de l'exemple
if __name__ == "__main__":
    exemple_k3()

# fin, fait pour k=4 aussi