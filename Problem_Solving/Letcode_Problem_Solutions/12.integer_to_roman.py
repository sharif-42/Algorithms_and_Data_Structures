class Solution(object):
    def intToRoman(self, num):
        if num==0:
            return ''
        roman_to_integer = {
            'M': 1000,
            'CM': 900,
            'D': 500,
            'CD': 400,
            'C': 100,
            'XC': 90,
            'L': 50,
            'XL': 40,
            'X': 10,
            'IX': 9,
            'V': 5,
            'IV': 4,
            'I': 1,
        }
        str = ''
        for k, v in roman_to_integer.items():
            rem = num % v
            div = num // v
            if rem == 0:
                str += k * div
                return str
            else:
                num = rem
                str += k * div

        return str


if __name__ == '__main__':
    num = 4
    sln = Solution().intToRoman(num)
    print(sln)
