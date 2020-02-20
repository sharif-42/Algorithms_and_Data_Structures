class Solution:
    def myPow(self, x: float, n: int) -> float:
        return round(x ** n, 5)


if __name__ == '__main__':
    x, n = 10, -2
    sln = Solution()
    sln = sln.myPow(x, n)
    print(sln)
