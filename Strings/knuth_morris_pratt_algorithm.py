

def kmp(string):
    j = 1
    result = [0] * len(string)
    while j < len(result):
        i = j - 1
        if result[i] > 0:
            t = result[i]
            if string[t] == string[j]:
                result[j] = t + 1
                j += 1
                continue
        if string[0] == string[j]:
            result[j] += 1
        j += 1
    return result


def main():
    string = 'ABCABABCA'
    string = 'ABACABADABA'
    result = kmp(string)
    print(*result)


if __name__ == '__main__':
    main()
