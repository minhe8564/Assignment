from numpy import array, zeros

def gauss(A, b):
    n = len(A)
    for i in range(n):
        # 부분 피봇팅
        pivot = i
        for j in range(i + 1, n):
            if abs(A[j, i]) > abs(A[pivot, i]):
                pivot = j
        A[[pivot, i]] = A[[i, pivot]]
        b[[pivot, i]] = b[[i, pivot]]

        # 전방 소거
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i + 1:] -= factor * A[i, i + 1:]
            b[j] -= factor * b[i]

    # 후방 대입법
    x = zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(A[i, i + 1:] * x[i + 1:])) / A[i, i]

    # A를 변환된 상삼각행렬의 형태로 수정
    for i in range(n):
        for j in range(i):
            A[i][j] = 0

    with open('gauss_out.txt', 'w') as f:
        for row in A:
            f.write(' '.join(['%.5f' % val for val in row]) + '\n')
        f.write('\n')

    return x


# 파일 읽기
with open('gauss_in.txt', 'r') as f:
    data = f.read()
lines = data.strip().split('\n\n')

A = array([list(map(float, row.split())) for row in lines[0].split('\n')])
b = array(list(map(float, lines[1].split())))
n = len(b)

x = gauss(A, b)

# 파일 쓰기
with open('gauss_out.txt', 'a') as f:
    for i in range(n):
        f.write('x%d = %.5f ' % (i+1, x[i]))
