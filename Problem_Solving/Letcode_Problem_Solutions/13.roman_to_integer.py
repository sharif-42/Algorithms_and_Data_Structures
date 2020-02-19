class Solution(object):

    def romanToInt(self, s):
        sum, i = 0, 0
        roman_to_integer = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900
        }

        n = len(s)
        if n == 0:
            return 0
        try:
            while i < n:
                ss = s[i] + s[i + 1]
                val = roman_to_integer.get(ss, 0)
                if val == 0:
                    sum += roman_to_integer[s[i]]
                else:
                    sum += val
                    i = i + 1
                i += 1
            return sum
        except:
            return sum+roman_to_integer[s[n-1]]


if __name__ == '__main__':
    s = "MMMMCMXCIV"
    sln = Solution().romanToInt(s)
    print(sln)
