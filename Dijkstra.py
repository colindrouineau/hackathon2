import numpy as np

adj_dic = {
    "A": ["B", "C"],
    "B": ["A"],
    "C": ["H", "G", "E", "A"],
    "D": ["F"],
    "E": ["C", "F"],
    "F": ["E", "D"],
    "G": ["H", "C"],
    "H": ["C", "G"],
}


def minimum_key(dico):
    """retourne la clé du dictionnaire qui a la valeur minimal"""
    min = np.inf
    cle = "aucune clé"
    for c in dico:
        if dico[c] < min:
            min = dico[c]
            cle = c
    min = np.inf
    return cle


def dijkstra(depart, adj_dic):
    """Renvoie distance_dic qui répérorie la distance entre le sommet et départ (les arrêtes ont toutes 1 pour distance)"""

    dist_pile = {
        depart: 0
    }  # C'est le dictionnaire qui va faire office de pile, on va le vider dans distnace_dic
    distance_dic = (
        {}
    )  # On met les sommets avec leur distance dans ce dico lorsqu'on est sûr d'avoir trouvé le distance minimale
    while dist_pile:
        sommet = minimum_key(
            dist_pile
        )  # On ajoute le sommet le plus proche dans le dico des distanceS En effet comme c'est le sommet le plus proche, on connais forcément sa distance, on ne peut pas aller plus vite en passant par un autre sommet parce que c'est le plus proche.
        distance = dist_pile.pop(sommet)  # On supprime l'élément de la pile
        distance_dic[sommet] = distance
        for adj in adj_dic[
            sommet
        ]:  # On veut ajouter certains sommets à la pile sous certaines conditions
            if not (adj in distance_dic):
                if adj in dist_pile:
                    if (
                        distance + 1 < dist_pile[adj]
                    ):  # Lorsque les sommets sont dans le distance_dic on ne les prend pas en compte
                        dist_pile[adj] = distance + 1
                else:
                    dist_pile[adj] = distance + 1
    return distance_dic


def chemin(depart, arrivee, adj_dic):
    poids = dijkstra(
        depart, adj_dic
    )  # liste des distances au départ (on va partir de l'arrivée pour arriver eu départ)
    position = arrivee  # On initialise la position à l'arrivée
    C = [arrivee]  # liste contenant les différentes positions
    while (
        poids[position] != 0
    ):  # On veut arriver au départ (pour lequel la distance au départ est 0)
        # On va créer un sous dico de poids qui contient les adjacent de position
        dico = {}
        for vertex in adj_dic:
            if position in adj_dic[vertex]:
                dico[vertex] = poids[vertex]
        position = minimum_key(dico)
        C.append(position)
    return C


print(chemin("H", "B", adj_dic))
print(dijkstra("H", adj_dic))
