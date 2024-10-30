"""
EULERIANCYCLE(Graph)
        form a cycle Cycle by randomly walking in Graph (don't visit the same edge twice!)
        while there are unexplored edges in Graph
            select a node newStart in Cycle with still unexplored edges
            form Cycle’ by traversing Cycle (starting at newStart) and then randomly walking
            Cycle ← Cycle’
        return Cycle
"""

import random
# pour faire de la marche aleatoire en choisissant les noeuds de maniere random

def cycle_eulerien(graphe):
    # copie des arêtes non visitées dans un dict dict
    aretes_restantes = {}
    for noeud in graphe:
        aretes_restantes[noeud] = graphe[noeud].copy()
    
    # s'il reste des arêtes à visiter
    def reste_des_aretes():
        for noeud in aretes_restantes:
            if aretes_restantes[noeud]:  # liste des voisins non vide
                return True
        return False
    
    # marche aléatoire le graphe
    def marche_aleatoire(depart):
        chemin = [depart]
        noeud_actuel = depart
        # boucle while : tant qu'il y a des aretes restantes, on choisit les noeuds de maniere random et on remplit la liste chemin
        while aretes_restantes[noeud_actuel]:
            prochain_noeud = random.choice(aretes_restantes[noeud_actuel])
            aretes_restantes[noeud_actuel].remove(prochain_noeud)
            noeud_actuel = prochain_noeud
            chemin.append(noeud_actuel)
        return chemin
    
    # On choisit un noeud de départ qui a des voisins
    noeuds_possibles = []
    for node in graphe:
        if graphe[node]:  # Si voisins il y a
            noeuds_possibles.append(node)
    noeud_depart = random.choice(noeuds_possibles)
    
    # premier cycle
    cycle = marche_aleatoire(noeud_depart)
    while reste_des_aretes():
        for pos, node in enumerate(cycle):
            if aretes_restantes[node]:  # Si on trouve un tel noeud
                # On commence par ce noeud, puis marche aleatoire
                nouveau_cycle = cycle[pos:] + cycle[1:pos+1]
                suite_du_cycle = marche_aleatoire(node)[1:]
                cycle = nouveau_cycle + suite_du_cycle
                break
    
    return cycle


input1 = {
    0: [3], 1: [0], 2: [1, 6], 3: [2], 4: [2],
    5: [4], 6: [5, 8], 7: [9], 8: [7], 9: [6]
}

graphe = input1
cycle = cycle_eulerien(graphe)

print('->'.join(str(edge) for edge in cycle))