import heapq

n = 3


def h0(S1, S2):  # Une heuristique naïve
    res = 0
    for i in range(n * n):
        res += S1[i] != S2[i]  # Sommer des booléens impose de les convertir en int
    return res


def h1(S1, S2):  # Somme des distances des chiffres
    loc1 = {}
    loc2 = {}
    for i in range(n * n):
        loc1[S1[i]] = [i // n, i % n]
        loc2[S2[i]] = [i // n, i % n]
    res = 0
    for j in range(n * n):
        res += abs(loc1[j][0] - loc2[j][0]) + abs(loc1[j][1] - loc2[j][1])
    return res


def hzero(S1, S2):
    return 0


import heapq
from collections import defaultdict


def astar(start, goal, graph, heuristic):
    open_list = [(0, start)]
    closed_list = set()
    g_scores = defaultdict(lambda: float("inf"))
    parents = defaultdict(lambda: None)

    g_scores[start] = 0
    i = 0

    while open_list:
        i += 1
        f_score, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]

        closed_list.add(current)

        for neighbor in graph[current]:
            if neighbor in closed_list:
                continue

            tentative_g_score = g_scores[current] + 1

            if tentative_g_score < g_scores[neighbor]:
                heapq.heappush(
                    open_list, (tentative_g_score + heuristic(neighbor, goal), neighbor)
                )
                parents[neighbor] = current
                g_scores[neighbor] = tentative_g_score

    return None


if __name__ == "__main__":
    S1 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    S2 = [1, 6, 8, 7, 5, 2, 3, 4, 0]

    print(h0(S1, S2))
    print(h1(S1, S2))
