class Solution:
    def _make_string(self, st, is_hash=False):
        d = {
            '1': 'a',
            '2': 'b',
            '3': 'c',
            '4': 'd',
            '5': 'e',
            '6': 'f',
            '7': 'g',
            '8': 'h',
            '9': 'i',
            '10': 'j',
            '11': 'k',
            '12': 'l',
            '13': 'm',
            '14': 'n',
            '15': 'o',
            '16': 'p',
            '17': 'q',
            '18': 'r',
            '19': 's',
            '20': 't',
            '21': 'u',
            '22': 'v',
            '23': 'w',
            '24': 'x',
            '25': 'y',
            '26': 'z',
        }
        new_s = ""
        if is_hash:
            new = d[st[-2:]]
            for i in range(2, len(st)):
                new_s = new_s + d[st[i - 2]]
            new_s += new
        else:
            for i in st:
                new_s = new_s + d[i]
        return new_s

    def freqAlphabets(self, s: str) -> str:
        new_s = ""
        n = ''
        for i in s:
            if i == '#':
                new_s += self._make_string(n, is_hash=True)
                n = ''
            else:
                n += i
        if n:
            new_s += self._make_string(n, is_hash=False)
        return new_s


if __name__ == "__main__":
    s = "10#11#12"
    s = Solution().freqAlphabets(s=s)
    print(s)
