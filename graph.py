# Les états sont codés sous forme de tuple : (1,2,3,4,5,6,0,7,8)


# afficher un état
def display(s):
    n = int(len(s) ** 0.5)
    for i in range(n):
        print([s[n * i + j] for j in range(n)])
    print()


# renvoie un état où pos1 et pos2sont échangés
def swap(s, pos1, pos2):
    new_state = []
    for i in range(len(s)):
        if i == pos1:
            new_state.append(s[pos2])
        elif i == pos2:
            new_state.append(s[pos1])
        else:
            new_state.append(s[i])
    return tuple(new_state)


# Argument : état s
# Sortie : Liste des états voisins
def list_of_neighbours(s):
    n = int(len(s) ** 0.5)
    position_of_0 = 0
    while s[position_of_0] != 0:
        position_of_0 += 1
    neighbours = []
    if position_of_0 % n != 0:
        neighbours.append(swap(s, position_of_0, position_of_0 - 1))
    if position_of_0 % n != n - 1:
        neighbours.append(swap(s, position_of_0, position_of_0 + 1))
    if position_of_0 // n != 0:
        neighbours.append(swap(s, position_of_0, position_of_0 - n))
    if position_of_0 // n != n - 1:
        neighbours.append(swap(s, position_of_0, position_of_0 + n))
    return neighbours


# crée une liste de tous les états possibles (9! ~ 3*10e5)
def all_states(n):
    def aux(s):
        if len(s) == 1:
            return [s]
        else:
            l = []
            for i in range(len(s)):
                for little_state in aux(s[:i] + s[i + 1 :]):
                    l.append([s[i]] + little_state)
            return l

    L = aux([i for i in range(n**2)])
    return [tuple(state) for state in L]


# Graphe total sous forme de dictionnaire d'adjacence
def generate_full_graph(n):
    keys = all_states(n)
    return {vertex: list_of_neighbours(vertex) for vertex in keys}


# Composante connexe à partir d'un sommet
# Complexité
def connected_graph(s):
    n = int(len(s) ** 0.5)
    d = {}
    visited = {vertex: False for vertex in all_states(n)}
    visited[s] = True
    pile = [s]
    while len(pile) > 0:
        state = pile.pop()
        neighbours = list_of_neighbours(state)
        d[state] = neighbours
        for neighbour in neighbours:
            if not visited[neighbour]:
                visited[neighbour] = True
                pile.append(neighbour)
    return d


def DFS(G, s0, visited):
    cc = []
    visited[s0] = True
    pile = [s0]
    while len(pile) > 0:
        vertex = pile.pop()
        cc.append(vertex)
        neighbours = G[vertex]
        for neighbour in neighbours:
            if not visited[neighbour]:
                visited[neighbour] = True
                pile.append(neighbour)
    return cc


# renvoie le nombre de composantes connexes de G et leurs tailles
# G est un dictionnaire d'adjacence
def connected_components(G):
    ccs = []
    available_vertices = list(G.keys())
    visited = {vertex: False for vertex in G}
    while len(available_vertices) > 0:
        ccs.append(DFS(G, available_vertices[0], visited))
        assert True in visited.values()
        av = []
        for v in available_vertices:
            if not visited[v]:
                av.append(v)
        available_vertices = av
    return [len(cc) for cc in ccs]
