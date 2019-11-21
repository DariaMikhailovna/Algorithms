def insertion_sort(arr):
    for j in range(len(arr)):
        cur = arr[j]
        i = j - 1
        while i >= 0 and cur < arr[i]:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = cur
    return arr


if __name__ == '__main__':
    print(*insertion_sort([4, 3, 5, 2, 1]))
    print(*insertion_sort([4]))
    print(*insertion_sort([]))
