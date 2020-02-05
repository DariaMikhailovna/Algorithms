import os


def number_to_byte(num):
    assert -128 <= num <= 127
    return int.to_bytes(num, byteorder='little', signed=True, length=1)


def byte_to_number(byte):
    return int.from_bytes(bytes([byte]), byteorder='little', signed=True)


def zip_bytes(arr):
    assert type(arr) == bytes
    res = b''
    cnt = 1
    for i in range(len(arr)):
        if i == len(arr) - 1:
            res += number_to_byte(cnt) + arr[i:i + 1]
            break
        if arr[i] == arr[i + 1]:
            cnt += 1
            if int(cnt) == 128:
                res += number_to_byte(127) + arr[i:i + 1]
                cnt = 1
        else:
            res += number_to_byte(cnt) + arr[i:i + 1]
            cnt = 1
    final_res = b''
    i = 0
    cnt = 0
    s = b''
    while i < len(res):
        j = i
        while j < len(res) and 1 <= byte_to_number(res[j]) <= 2:
            num = byte_to_number(res[j])
            cnt += num
            s += res[j + 1:j + 2] * num
            if cnt >= 128:
                final_res += number_to_byte(-128)
                cnt -= 128
                final_res += s[:128]
                s = s[128:]
            j += 2
        if j == i:
            final_res += res[i:i + 2]
            i += 2
        else:
            if cnt > 0:
                final_res += number_to_byte(-cnt) + s
            cnt = 0
            s = b''
            i = j
    return final_res


def unzip_bytes(arr):
    res = b''
    i = 0
    while i < len(arr):
        num = byte_to_number(arr[i])
        i += 1
        if num > 0:
            res += arr[i:i + 1] * num
            i += 1
        else:
            num = -num
            res += arr[i:i + num]
            i += num
    return res


def zip_file(file_in, file_out):
    with open(file_in, 'rb') as f:
        data = f.read()
    data_zipped = zip_bytes(data)
    with open(file_out, 'wb') as f:
        f.write(data_zipped)


def unzip_file(file_in, file_out):
    with open(file_in, 'rb') as f:
        data_zipped = f.read()
    data = unzip_bytes(data_zipped)
    with open(file_out, 'wb') as f:
        f.write(data)


def main():
    arrs = [
        b'#########....#.###.#.#.##..#...#########',
        b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',
        b'abcdefghjuydlgindfjlabcdefghjuydlgindfjlabcdefghjuydlgindfjlabcdefghjuydlgindfjlabcdefghjuydlgindfjlabcdefghjuydlgindfjlabcdefghjuydlgindfjl',
        b'ddj3lk45kkkf',
        b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab',
        b'abababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababab',
        b'ababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababababb',
    ]
    for arr in arrs:
        res_zipped = zip_bytes(arr)
        print(res_zipped)
        res_unzipped = unzip_bytes(res_zipped)
        print(res_unzipped)
        assert res_unzipped == arr

    # filename = 'test_image.png'
    filename = 'file.bmp'
    filename_zipped = 'zipped_' + filename + '.bin'
    filename_unzipped = 'unzipped_' + filename

    zip_file(filename, filename_zipped)
    unzip_file(filename_zipped, filename_unzipped)
    print(os.path.getsize(filename))
    print(os.path.getsize(filename_zipped))


if __name__ == '__main__':
    main()
