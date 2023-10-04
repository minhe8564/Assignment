def quicksort(arr):
    if len(arr) <=1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

# 파일 읽기
with open('input_quick_sort.txt', 'r') as f:
    data = [int(line.strip()) for line in f]

sorted_data = quicksort(data)

# 파일 쓰기
with open('output_quick_sort.txt', 'w') as f:
    for num in sorted_data:
        f.write(str(num) + '\n')

print(sorted_data)
