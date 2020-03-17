import random as rnd


def bucket_sort(arr, k):
    mx = max(arr)
    mn = min(arr)
    if mx == mn:
        return arr
    buckets = [[] for i in range(k)]
    for numb in arr:
        if numb == mx:
            t = k - 1
        else:
            t = (k * numb) // (mx - mn)
        buckets[t].append(numb)
    for b in range(k):
        buckets[b] = bucket_sort(buckets[b], k)
    i = 0
    for b in buckets:
        for numb in b:
            arr[i] = numb
            i += 1
    return arr


def main(count_numbers):
    arr = [1, 25, 5, 70, 7, 9, 100, 2, 4, 6, 8, 90, 0, 35, 59, ]
    bucket_sort(arr, 2)
    print(*arr)
    # arr = []
    # for i in range(count_numbers):
    #     arr.append(rnd.randint(0, 65535))


if __name__ == '__main__':
    main(10000)
