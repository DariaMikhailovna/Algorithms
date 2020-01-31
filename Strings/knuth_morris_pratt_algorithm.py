
def kmp(string):
    result = [0] * len(string)
    for j in range(len(result)):
        i = j
        while i > 0:
            t = result[i - 1]
            if string[t] == string[j]:
                result[j] = t + 1
                break
            else:
                i = t
    return result


def is_pattern_in_text(pattern, text):
    res = kmp(pattern + '$' + text)
    pattern_len = len(pattern)
    for i in range(pattern_len + 1, len(res)):
        if res[i] == pattern_len:
            return i - 2 * pattern_len
    return False


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
    index_or_false = is_pattern_in_text('ca', 'csfdcab')
    print(index_or_false)


if __name__ == '__main__':
    main()
