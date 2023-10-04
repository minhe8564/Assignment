from numpy import *

def luDecomposition(mat, n):
    L = [[0 for x in range(n)]
             for y in range(n)]
    U = [[0 for x in range(n)]
             for y in range(n)]

    for i in range(n):
        # upper
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (L[i][j] * U[j][k])
            U[i][k] = mat[i][k] - sum

        # lower
        for k in range(i, n):
            if (i == k):
                L[i][i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += (L[k][j] * U[j][i])
                L[k][i] = (mat[k][i] - sum) / U[i][i]

    return L, U
