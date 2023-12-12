import numpy as np
import time
from heapq import *
from collections import defaultdict

#서울 = 0, 천안 = 1, 원주 = 2, 강릉 = 3, 논산 = 4,
#대전 = 5, 대구 = 6, 포항 = 7, 광주 = 8, 부산 = 9
input = [[0,1,12],[0,2,15],[1,4,4],[1,5,10],[2,3,21],
         [2,6,7], [3,7,25],[4,5,3],[4,8,13],[5,6,10],
         [6,7,19],[6,9,9] ,[7,9,5],[8,9,15]]

n = 10

def Dijkstra(G, start):
    D = defaultdict(list)
    for p, v, weight in G:
        D[p].append((weight, p, v))
        D[v].append((weight, v, p))
    
    Weight = [float('inf')]*n
    T_visited = set()
    nextNode = set()
    
    Weight[start] = 0
    selectV = D[start]
    heapify(selectV)
    nextNode.add(selectV[0][2])
    
    while selectV:
        weight, p, v = heappop(selectV)
        if Weight[v] > Weight[p] + weight:
            Weight[v] = Weight[p] + weight
            nextNode.add(v)
            
        if len(selectV) == 0:
            T_visited.add(p)
            temp = [99999,-1]     
            for next in nextNode:
                if next not in T_visited:
                    if Weight[next] < temp[0]:
                        temp[0] = Weight[next]
                        temp[1] = next
        
            if temp[1] != -1:
                for edge in D[temp[1]]:
                    heappush(selectV, edge)
                nextNode.remove(temp[1])
                   
    return Weight

output = []

startT = time.perf_counter_ns()
for i in range(n):
    output.append(Dijkstra(input, i))
endT = time.perf_counter_ns()

out = np.array(output)
lastOut = np.triu(out, k = 1)

print(lastOut)
print(endT - startT)
