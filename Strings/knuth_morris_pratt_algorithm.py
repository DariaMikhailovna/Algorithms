
def kmp(string):
    result = [0] * len(string)
    for j in range(1, len(result)):
        i = j
        while i > 0:
            t = result[i - 1]
            if string[t] == string[j]:
                result[j] = t + 1
                break
            else:
                i = t
    return result


def main():
    string = 'ABCABABCA'
    string = 'ABACABADABA'
    string = 'ABACABAB'
    string = 'AABAAA'
    string = 'ABACABAB'
    string = 'abcabcd'
    string = 'aabaabb'
    result = kmp(string)
    print(*result)


if __name__ == '__main__':
    main()
