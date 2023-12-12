import time

path = "./algorithm/"
input = [int(line.strip()) for line in open(path + 'input.txt', 'r', encoding='UTF-8')]
# input = [5, 4, 3, 2, 1]

def elapsed(func):
    def elapsed_wrapper(*args, **kwargs):
        s = time.perf_counter()
        func(*args, **kwargs)
        e = time.perf_counter()
        total = e - s
        print(f"{total:.6f} seconds!!")
    return elapsed_wrapper

def heapify(arr, i, n):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left
    
    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, n)

def build_heap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)

@elapsed
def heap_sort(arr):
    n = len(arr)
    build_heap(arr, n)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, 0, i)


heap_sort(input)

f = open(path + 'output.txt', 'w', encoding='UTF-8')
for line in input:
    f.write(str(line) + '\n')
