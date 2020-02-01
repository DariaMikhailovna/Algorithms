from collections import defaultdict


class BoyerMoore:
    def __init__(self, pattern):
        self.pattern = pattern
        self.prefix_table = self.prefix()
        self.suffix_table = self.suffix()

    def prefix(self):
        d = defaultdict(lambda: -1)
        for i in range(len(self.pattern)):
            d[self.pattern[i]] = i
        return d

    def suffix(self):
        pattern_len = len(self.pattern)
        res = [0] * pattern_len
        for suffix_len in range(pattern_len):
            for str_end in range(pattern_len - 1, -1, -1):
                ok = True
                for suf_index in range(suffix_len):
                    if str_end - suf_index - 1 < 0:
                        break
                    if self.pattern[str_end - suf_index - 1] != self.pattern[pattern_len - suf_index - 1]:
                        ok = False
                        break
                if ok:
                    res[pattern_len - suffix_len - 1] = pattern_len - str_end
                    break
        return res

    def calc_shift(self, symbol_number):
        return max(1, self.prefix_table[self.pattern[symbol_number]], self.suffix_table[symbol_number])

    def run(self, text):
        offset = 0
        while offset + len(self.pattern) <= len(text):
            for symbol_number in range(len(self.pattern) - 1, -1, -1):
                if self.pattern[symbol_number] != text[offset + symbol_number]:
                    offset += self.calc_shift(symbol_number)
                    break
            else:
                return offset
        return False


def main():
    string = 'CABABCAB'
    pattern = 'ABACABADABACABA'
    # pattern = 'ab'
    # pattern = 'aba'
    bm = BoyerMoore(pattern)
    print(bm.run(string))


if __name__ == '__main__':
    main()
