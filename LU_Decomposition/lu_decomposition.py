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

# 파일 읽기
with open('LU_in.txt', 'r') as f:
    data = f.read()

lines = data.strip().split('\n\n')

# Ax = b
A = array([list(map(float, row.split())) for row in lines[0].split('\n')])
b = array(list(map(float, lines[1].split())))
n = len(b)

# LU 분해, LUx = y
L, U = luDecomposition(A, n)

# y
y = zeros(n)
for i in range(n):
    y[i] = b[i]
    for j in range(i):
        y[i] = y[i] - (L[i][j] * y[j])
    y[i] = y[i] / L[i][i]

# x
x = zeros(n)
for i in range(n-1, -1, -1):
    x[i] = y[i]
    for j in range(i+1, n):
        x[i] = x[i] - U[i][j] * x[j]
    x[i] = x[i] / U[i][i]

# 파일 쓰기
with open('LU_out.txt', 'w') as f:
    # LU
    for i in range(n):
        for j in range(n):
            f.write('%.5f ' % L[i][j])
        f.write('\t')

        for j in range(n):
            f.write('%.5f ' % U[i][j])
        f.write('\n')

    f.write('\n')

    f.write('y ')
    for i in range(n):
        f.write('%.5f ' % y[i])
    f.write('\n\n')

    for i in range(n):
        f.write('x%d = %.5f ' % (i+1, x[i]))
