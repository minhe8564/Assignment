import numpy as np
import time

#서울 = 0, 천안 = 1, 원주 = 2, 강릉 = 3, 논산 = 4,
#대전 = 5, 대구 = 6, 포항 = 7, 광주 = 8, 부산 = 9
n = 10
input = [[0,1,12],[0,2,15],
         [1,4,4],[1,5,10],
         [2,3,21],[2,6,7],
         [3,7,25],
         [4,5,3],[4,8,13],
         [5,6,10],
         [6,7,19],[6,9,9],
         [7,9,5],
         [8,9,15]]

def Floyd(input):
    Weight = [[float('inf')]*n for _ in range(n)]
    
    for i in input:
        if Weight[i[0]][i[1]] > i[2]:
            Weight[i[0]][i[1]] = i[2]
            Weight[i[1]][i[0]] = i[2]
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != k and j != k and j != i:
                    Weight[i][j] = min(Weight[i][j], Weight[i][k] + Weight[k][j])
    
    return Weight

startT = time.perf_counter_ns()
output = Floyd(input)
endT = time.perf_counter_ns()

out = np.array(output)
lastOut = np.triu(out, k = 1)

print(lastOut)
print(endT - startT)
