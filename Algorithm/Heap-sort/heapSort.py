def downHeap(arr, i, n):
  leftChild = 2 * i
  rightChild = 2 * i + 1

  if leftChild <= n and arr[leftChild] >  arr[i]:
    bigger = leftChild
  else:
    bigger = i
  if rightChild <= n and arr[rightChild] > arr[bigger]:
    bigger = rightChild
  if bigger != i:
    arr[i], arr[bigger] = arr[bigger], arr[i]
    downHeap(arr, bigger, n)

def buildHeap(arr, n):
  for i in range(n // 2, -1, -1):
    downHeap(arr, i, n)

def heapSort(arr):
  n = len(arr) - 1
  buildHeap(arr, n)
  for i in range(n, 0, -1):
    arr[i], arr[0] = arr[0], arr[i]
    downHeap(arr, 0, i - 1)

with open("/content/input.txt", 'r') as file:
  numbers = file.read().split()
  arr = [int(num) for num in numbers]

heapSort(arr)

with open("/content/output.txt", 'w') as file:
  for num in arr:
    file.write(str(num) + '\n')