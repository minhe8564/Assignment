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
