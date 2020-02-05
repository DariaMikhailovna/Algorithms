
def zip_array(arr):
    res = ''
    cnt = 1
    for i in range(len(arr)):
        if i == len(arr) - 1:
            res += str(cnt) + arr[i]
            break
        if arr[i] == arr[i + 1]:
            cnt += 1
            if int(cnt) == 128:
                res += str(127) + arr[i]
                cnt = 1
        else:
            res += str(cnt) + arr[i]
            cnt = 1
    res2 = ''
    i = 0
    cnt = 0
    s = ''
    while i < len(res):
        j = i
        while j < len(res) and res[j].isdigit() and not res[j + 1].isdigit() and (res[j] == '1' or res[j] == '2'):
            cnt += int(res[j])
            s += res[j + 1]
            if res[j] == '2':
                s += res[j + 1]
            if cnt == 128:
                res2 += '-' + str(cnt)
                cnt = 0
                res2 += s
                s = ''
            j += 2
        if j == i:
            res2 += res[i]
            i += 1
        else:
            res2 += '-' + str(cnt) + s
            cnt = 0
            s = ''
            i = j
    return res2


def dezip_array(arr):
    res = ''
    i = 0
    while i < len(arr):
        coef = ''
        while arr[i].isdigit():
            coef += arr[i]
            i += 1
        if coef:
            for j in range(int(coef)):
                res += arr[i]
        if arr[i] == '-':
            i += 1
            coef = ''
            while arr[i].isdigit():
                coef += arr[i]
                i += 1
            j = 0
            while j < int(coef):
                res += arr[i + j]
                j += 1
            i += j
            continue
        i += 1
    return res


def zip_file(file):
    pass


def dezip_file(file):
    pass


def main():
    arr = '#########....#.###.#.#.##..#...#########'
    arr = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
    arr = 'abcdefghjuydlgindfjlabcdefghjuydlgindfjlabcdefghjuydlgindfjlabcdefghjuydlgindfjlabcdefghjuydlgindfjlabcdefghjuydlgindfjlabcdefghjuydlgindfjl'
    arr = 'zip-архив и написать вывод. + 2 байта Вариант А. Алгоритм RLE. 1.'
    arr = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
    res_zip = zip_array(arr)
    print(res_zip)
    res_dezip = dezip_array(res_zip)
    print(res_dezip)
    assert arr == res_dezip


if __name__ == '__main__':
    main()
