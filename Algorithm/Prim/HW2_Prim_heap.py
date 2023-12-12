import random
import heapq

input = [(0, 1, 3), (0, 4, 4), (0, 3, 2), (3, 4, 5), (3, 1, 4), (4, 5, 9), (3, 5, 7), (1, 5, 2), (1, 2, 1), (2, 5, 1)]
random.shuffle(input)
input.sort(key = lambda x: (x[2], x[0], x[1]))

parent = [i for i in range(0, 26)]

def PrimMst(G):
    visited = [0 for _ in range(0, 26)]
    graph = [[] for _ in range(0, 26)]
    mst = []

    for t in G:
        graph[t[0]].append((t[2], t[0], t[1]))
        graph[t[1]].append((t[2], t[1], t[0]))

    hq = graph[2]
    heapq.heapify(hq)
    visited[2] = 1
    
    while hq:
        w, u, v = heapq.heappop(hq)
        if visited[v]:
            continue
        mst.append((u, v, w))
        visited[v] = 1

        for e in graph[v]:
            if visited[e[2]]:
                continue

            heapq.heappush(hq, (e[0], e[1], e[2]))
            
    return mst


for t in PrimMst(input):
    print(t, end='\n')
