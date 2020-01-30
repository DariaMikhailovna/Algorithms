
def kmp(string):
    result = [0] * len(string)
    for j in range(1, len(result)):
        i = j - 1
        while result[i] > 0:
            t = result[i]
            if string[t] == string[j]:
                result[j] = t + 1
                break
            else:
                i = t - 1
        if result[j] == 0 and string[0] == string[j]:
            result[j] += 1
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
