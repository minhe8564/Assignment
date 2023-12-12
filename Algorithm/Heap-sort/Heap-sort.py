def buildHeap(A):
    heapSize = len(A) - 1
    for i in range(heapSize // 2, -1, -1):
        downHeap(A, i, heapSize)

def downHeap(A, i, heapSize):
    leftChild = 2 * i + 1
    rightChild = 2 * i + 2

    if leftChild <= heapSize and A[leftChild] > A[i]:
        bigger = leftChild
    else:
        bigger = i

    if rightChild <= heapSize and A[rightChild] > A[bigger]:
        bigger = rightChild

    if bigger != i:
        A[i], A[bigger] = A[bigger], A[i]
        downHeap(A, bigger, heapSize)

def heapSort(A):
    buildHeap(A)

    heapSize = len(A) - 1
    for i in range(heapSize, 0, -1):
        A[0], A[i] = A[i], A[0]
        heapSize -= 1
        downHeap(A, 0, heapSize)

# 파일 읽기
with open('input.txt', 'r') as f:
    A = [0] + list(map(int, f.read().split()))

heapSort(A)

# 파일 쓰기
with open('output.txt', 'w') as f:
    f.write('\n'.join(map(str, A[1:])))

print(A[1:])
