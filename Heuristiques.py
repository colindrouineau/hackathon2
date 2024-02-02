n = 3

def h0(S1, S2):         #Une heuristique naïve
    res = 0
    for i in range(n*n):
        res += (S1[i] != S2[i])   #Sommer des booléens impose de les convertir en int
    return res

def h1(S1, S2):
    loc1 = {}
    loc2 = {}
    for i in range(n*n):
        loc1[S1[i]] = [i//n, i%n]
        loc2[S2[i]] = [i//n, i%n]
    res = 0
    for j in range(n*n):
        res += abs(loc1[j][0] - loc2[j][0]) + abs(loc1[j][1] - loc2[j][1])
    return res 

S1 = [0,1,2,3,4,5,6,7,8]
S2 = [1,6,8,7,5,2,3,4,0]

print(h0(S1,S2))
print(h1(S1,S2))

import heapq

def astar(start, goal, graph, heuristic):
    """
    A* algorithm implementation.
    Args:
        start: Start node.
        goal: Goal node.
        graph: Graph represented as a dictionary of lists.
        heuristic: Heuristic function.
    Returns:
        Path from start to goal.
    """
    # Initialize open and closed lists.
    open_list = [(0, start)]
    closed_list = set()
    # Initialize g-scores and parents.
    g_scores = {start: 0}
    parents = {start: None}
    while open_list:
        # Get node with lowest f-score.
        f_score, current = heapq.heappop(open_list)
        # Check if goal node is reached.
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parents[current]
            return path[::-1]
        # Add current node to closed list.
        closed_list.add(current)
        # Explore neighbors.
        for neighbor in graph[current]:
            # Ignore neighbors in closed list.
            if neighbor in closed_list:
                continue
            # Calculate tentative g-score.
            tentative_g_score = g_scores[current] + 1
            # Add neighbor to open list if not already in it.
            if neighbor not in [n[1] for n in open_list]:
                heapq.heappush(open_list, (tentative_g_score + heuristic(neighbor, goal), neighbor))
            # Update neighbor's g-score if new path is better.
            elif tentative_g_score < g_scores[neighbor]:
                index = [n[1] for n in open_list].index(neighbor)
                open_list[index] = (tentative_g_score + heuristic(neighbor, goal), neighbor)
            # Update parent and g-score.
            parents[neighbor] = current
            g_scores[neighbor] = tentative_g_score
    # No path found.
    return None

