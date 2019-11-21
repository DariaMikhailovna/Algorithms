def selection_sort(arr):
    for j in range(len(arr)):
        min_ind = j
        for i in range(j + 1, len(arr)):
            if arr[min_ind] > arr[i]:
                min_ind = i
        arr[j], arr[min_ind] = arr[min_ind], arr[j]
    return arr


if __name__ == '__main__':
    print(*selection_sort([4, 3, 5, 2, 1]))
    print(*selection_sort([4]))
    print(*selection_sort([]))

