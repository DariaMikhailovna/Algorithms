import random


def partition(arr, left, right):
    num = random.randint(left, right - 1)
    # num = left
    # num = right - 1
    # num = (left + right) // 2
    
    p = arr[num]
    arr[num], arr[right - 1] = arr[right - 1], arr[num]
    i = left
    j = left
    while j < right:
        if arr[j] > p:
            j += 1
            continue
        else:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            j += 1
    return i


def quick_sort(arr, left, right):
    if right - left <= 1:
        return
    center = partition(arr, left, right)
    quick_sort(arr, left, center - 1)
    quick_sort(arr, center, right)


if __name__ == '__main__':
    arr = [65, 12, 24, 50, 14, 30, 0, 1, 88, 34]
    print(quick_sort(arr, 0, len(arr)))
    print(arr)
