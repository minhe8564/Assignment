from numpy import *

def luDecomposition(mat, n):
    lower = [[0 for x in range(n)]
             for y in range(n)]
    upper = [[0 for x in range(n)]
             for y in range(n)]

    for i in range(n):
        # upper
        for k in range(i, n):
            sum = 0
            for j in range(i):
                sum += (lower[i][j] * upper[j][k])
            upper[i][k] = mat[i][k] - sum

        # lower
        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1
            else:
                sum = 0
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i])
                if upper[i][i] == 0:
                    lower[k][i] = 0
                else:
                    lower[k][i] = (mat[k][i] - sum) / upper[i][i]

    return lower, upper

# 파일 읽기
with open('LU_in.txt', 'r') as f:
    data = f.read()

lines = data.strip().split('\n\n')

# Ax = b
A = array([list(map(float, row.split())) for row in lines[0].split('\n')])
b = array(list(map(float, lines[1].split())))
n = len(b)

# LU 분해, LUx = y
lower, upper = luDecomposition(A, n)

# y
y = zeros(n)
for i in range(n):
    y[i] = b[i]
    for j in range(i):
        y[i] = y[i] - (lower[i][j] * y[j])
    y[i] = y[i] / lower[i][i]

# x
x = zeros(n)
for i in range(n-1, -1, -1):
    x[i] = y[i]
    for j in range(i+1, n):
        x[i] = x[i] - upper[i][j] * x[j]
    x[i] = x[i] / upper[i][i]

# 파일 쓰기
with open('LU_out.txt', 'w') as f:
    # LU
    for i in range(n):
        for j in range(n):
            f.write('%d ' % lower[i][j])
        f.write('\t')

        for j in range(n):
            f.write('%d ' % upper[i][j])
        f.write('\n')

    f.write('\n')

    f.write('y ')
    for i in range(n):
        f.write('%d ' % y[i])
    f.write('\n\n')

    for i in range(n):
        f.write('x%d = %.5f ' % (i+1, x[i]))
