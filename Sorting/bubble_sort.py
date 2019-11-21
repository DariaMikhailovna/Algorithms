def bubble_sort(arr):
    for j in range(len(arr)):
        for i in range(len(arr) - 1 - j):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


if __name__ == '__main__':
    print(*bubble_sort([4, 3, 5, 2, 1]))
    print(*bubble_sort([4]))
    print(*bubble_sort([]))
