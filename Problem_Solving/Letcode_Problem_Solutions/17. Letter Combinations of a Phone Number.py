class Solution:
    def letterCombinations(self, digits):
        values = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        


if __name__ == '__main__':
    num = 4
    digits = '23'
    sln = Solution().letterCombinations(digits)
    print(sln)
