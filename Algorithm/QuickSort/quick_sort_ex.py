# 분할 함수
def partition(arr, left, right):
    mid = (left + right) // 2
    arr[left], arr[mid] = arr[mid], arr[left]
    pivot = arr[left]

    i = left + 1
    j = right

    while True:
        while i <= j and arr[i] < pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            # pivot 기준으로 교환
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break

    arr[left], arr[j] = arr[j], arr[left]

    return j

# quicksort 함수, 재귀적으로 배열 정리
def quicksort(arr, left, right):
    if left < right:
        pivot_index = partition(arr, left, right)
        quicksort(arr, left, pivot_index - 1)
        quicksort(arr, pivot_index + 1, right)

# 파일 읽기
with open('input_quick_sort.txt', 'r') as f:
    data = list(map(int,f.read().split()))

# 데이터 정렬
quicksort(data ,0 ,len(data) -1)

# 파일 쓰기
print(data)
with open('output_quick_sort.txt', 'w') as f:
    for num in data:
        f.write(f"{num}\n")
