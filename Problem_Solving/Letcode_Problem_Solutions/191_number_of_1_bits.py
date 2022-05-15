class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n > 0:
            res += (n % 2)
            n //= 2
        return res


if __name__ == "__main__":
    n = '00000000000000000000000000001011'
    s = Solution().hammingWeight(n=n)