class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s = str(n)
        prod = 1
        sum = 0
        for i in s:
            digit = int(i)
            prod *= digit
            sum += digit
        diff = prod - sum
        return diff


if __name__ == "__main__":
    n = 4421
    s = Solution().subtractProductAndSum(n=n)
