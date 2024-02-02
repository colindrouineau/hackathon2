import numpy as np

adj_dic = {'A' : ['B', 'C'], 'B' : ['A'], 'C' : ['H', 'G', 'E'], 'D' : ['F'], 'E' : ['C','F'], 'F' : ['E', 'D'], 'G' : ['H', 'C'], 'H' : ['C', 'G']}

def minimum_key(dico):
    '''retourne la clé du dictionnaire qui a la valeur minimal'''
    min = np.inf
    cle = "aucune clé"
    for c in dico:
        if dico[c] < min:
            min = dico[c]
            cle = c
    min = np.inf
    return cle


def dijstra(depart, adj_dic):
    '''Renvoie distance_dic qui répérorie la distance entre le sommet et départ (les arrêtes ont toutes 1 pour distance)'''
    dist_pile = {depart : 0} # C'est le dictionnaire qui va faire office de pile, on va le vider dans distnace_dic
    distance_dic = {} # On met les sommets avec leur distance dans ce dico lorsqu'on est sûr d'avoir trouvé le distance minimale
    while dist_pile:
        sommet = minimum_key(dist_pile)  # On ajoute le sommet le plus proche dans le dico des distanceS En effet comme c'est le sommet le plus proche, on connais forcément sa distance, on ne peut pas aller plus vite en passant par un autre sommet parce que c'est le plus proche.
        distance = dist_pile.pop(sommet) # On supprime l'élément de la pile
        distance_dic[sommet] = distance
        for adj in (adj_dic[sommet]):  # On veut ajouter certains sommets à la pile sous certaines conditions
            if not(adj in distance_dic):
                if adj in dist_pile:
                    if distance + 1 < dist_pile[adj]: # Lorsque les sommets sont dans le distance_dic on ne les prend pas en compte
                        dist_pile[adj] = distance + 1
                else:
                    dist_pile[adj] = distance + 1
    return distance_dic

print(dijstra('A', adj_dic))
