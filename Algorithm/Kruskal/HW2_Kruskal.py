import random

input = [(1, 2, 1), (2, 5, 1), (1, 5, 2), (0, 3, 2), (3, 4, 3), (0, 4, 4), (1, 3, 4), (3, 5, 7), (0, 1, 8), (4, 5, 9)]
random.shuffle(input)
input.sort(key = lambda x: (x[2], x[0], x[1]))

parent = [i for i in range(0, 26)]

def UNION(u, v):
    u = FIND(u)
    v = FIND(v)
    parent[u] = v

def FIND(u):
    parent[u] = (u if parent[u] == u else FIND(parent[u]))
    return parent[u]

def KrsukalMST(G):
    mst = []
    for t in G:
        if FIND(t[0]) != FIND(t[1]):
            UNION(t[0], t[1])
            mst.append((t[0], t[1], t[2]))
 
    return mst


for t in KrsukalMST(input):
    print(t, end='\n')
