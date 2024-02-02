import Heuristiques as h
import graph as g

if __name__ == '__main__':
    print("Sommet de départ. Ex 012345678")
    s1 = input()
    start = tuple([int(s1[i]) for i in range(len(s1))])
    print("Sommet d'arrivée. Ex 012345678")
    s2 = input()
    goal = tuple([int(s2[i]) for i in range(len(s2))])

    g.display(start)
    g.display(goal)

    print(g.list_of_neighbours(start))

    subgraph = g.connected_graph(start)

    if s2 not in subgraph :
        print("Il n'existe pas de solution.")
    
    else :
        path = h.astar(start, goal, subgraph, h.h1)
        print("Nous avons trouvé une solution de taille", len(path))
        print("Voulez-vous l'afficher ? (y/n)")
        while c not in ["y","n"]:
            c = input()
        if c == "y":
            for state in path :
                g.display(state)