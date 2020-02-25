class Solution:
    def myPow(self, x, n):
        x = x ** n
        return x


def myPower(x, n):
    """
    :param x: float
    :param n: int
    :return:
    """
    if n == 0:
        return 1.0
    elif n < 0:
        return 1 / myPower(x, -n)
    elif n % 2:
        return myPower(x * x, n // 2) * x
    else:
        return myPower(x * x, n // 2)


if __name__ == '__main__':
    x, n = 2.10000, 3
    sln = Solution()
    sln = sln.myPow(x, n)
    print(myPower(x, n))
    print(sln)
